class Ope_Lista:
    def __init__(self,tamanio=3):
        self.lista = []
        self.longitud = 0
        self.size = tamanio
        
    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud +=1
            return self.lista
        else:
            print("Lista esta llena")
            
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]
        
    def buscar(self,dato):
        pass
    
    def insertar(sefl,dato):
        pass
    
    def eliminar(self,dato):
        pass
        
    def obtenerEliminado(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado = self.lista[pos]
            #self.lista = self.lista[:dato] + self.lista[dato+1:]
            listaAux = []
            for ind in range(pos):
                listaAux += [self.lista[ind]]
            for indice in range(pos+1,self.longitud):
                listaAux += [self.lista[indice]]
                self.longitud -= 1
                self.lista = listaAux
            return [self.lista,eliminado]
            
    
    def mostrar(self):
        print(" {:6} {}".format("lista","Posicion"))
        for pos, ele in enumerate(self.lista):
            print("[{:6}] {:3}".format(ele,pos))
            
# lista1 = Lista()
# lista1.append("Daniel")
# lista1.append(52)
# lista1.append(32)
# lista1.append("Milagro")
# lista1.mostrar()
# posicion=int(input("Ingrese posicion:"))
# resp = lista1.obtenerEliminado(posicion)
# if resp == None:
#     print("Posicion no Valida")
# else:
#     print("El elemento de la posicion: {} es: {}".format(posicion,resp))

