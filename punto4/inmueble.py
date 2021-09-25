class inmueble:

    def __init__(self,codigo,direccion,telefono):
        self.__codigo = codigo
        self.__direccion = direccion
        self.__telefono = telefono

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,valor):
        self.__codigo = valor
    
    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self,valor):
        self.__direccion = valor

    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,valor):
        self.__telefono = valor

    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ' - Direccion: ' + str(self.__direccion) + ' - Telefono: ' + str(self.__telefono)

inmueble1 = inmueble(1,"cra 36A #37-39","3197060463")
inmueble2 = inmueble(2,"cra 100B #90-43","3197080463")
inmueble3 = inmueble(3,"cra 40A #50-30","3197069463")

print(inmueble1.direccion)

print(inmueble2.codigo)

print(inmueble3.telefono)

