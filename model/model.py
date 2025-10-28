from database.DB_connect import get_connection
from model.automobile import Automobile

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
        self.__cnx = get_connection()
        self.__cursor = self.__cnx.cursor()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """

        # TODO
        self.__query = """SELECT * FROM automobile"""
        self.__cursor.execute(self.__query)
        self.__automobili = []
        for auto in self.__cursor:
            self.__automobili.append(Automobile(codice=auto[0], marca=auto[1], modello=auto[2], anno=auto[3], posti=auto[4]))
        return list(self.__automobili)

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        self.__query = f"""SELECT * FROM automobile WHERE modello = '{modello}'"""
        self.__cursor.execute(self.__query)
        self.__automobili = []
        for auto in self.__cursor:
            self.__automobili.append(
                Automobile(codice=auto[0], marca=auto[1], modello=auto[2], anno=auto[3], posti=auto[4]))
        return list(self.__automobili)
