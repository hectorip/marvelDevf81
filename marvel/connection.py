import requests # Peticiones http (get, post, put, delete)
import hashlib


class Marvel:
    ts = "1"
    key = "1fbc34ab2e589b14f11a719870ddc4bb"
    p_key = "6426d53ee843986cee028f338f922fd9d6acaba8"
    h = hashlib.md5((ts+p_key+key).encode()).hexdigest()
    url = "http://gateway.marvel.com/v1/public/"
    personaje = None

    @classmethod
    def getPersonaje(cls, personaje):
        try:
            response = requests.get(cls.url + "characters",
                params={
                    "apikey": cls.key,
                    "ts": cls.ts,
                    "hash": cls.h,
                    "name": personaje
                    }).json()
            # print(response.keys())
            data = response["data"]
            # print(data.keys())
            results = data["results"]
            cls.personaje = results[0]
            return "personaje {} agregado".format(personaje)
        except Exception as e:
            print(e)
            return "fail"

    @classmethod
    def getInfo(cls):
        for k, v in cls.personaje.items():
            if type(v) == dict:
                for c, val in v.items():
                    print("{}: \n {} \n \n".format(c, val))
            else:
                print("{}: \n {} \n \n".format(k, v))
         # imprimir

    @classmethod
    def openImage(cls):
        import webbrowser
        url = cls.personaje["thumbnail"]["path"]
        url = url + "." + cls.personaje["thumbnail"]["extension"]
        webbrowser.open(url)


