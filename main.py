class Fila(object):
    """Clase base de fila"""

    def __init__(self):            #Esto es el constructor de la clase
        """constructor de la clase Fila """
        self.enfila= 0                #esto me dice la cant de clientes que tengo en fila
        self.fila = []                #la fila prop. dicha es una lista, al comienzo vacía.

class FilaPreferencial(Fila):				  #Esta fila hereda los atributos de Fila
    """Clase de la fila de los clientes preferenciales""" #Si quisiera agregarle atributos debería agregar un constructo       
							  #con __init__
    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.fila.append(cliente)                          #appendea el cliente a la lista fila creada en __init__
        self.enfila += 1
        pass                                               #es como el continue en fortran

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1                                     #el SELF es una referencia al objeto
        self.fila.pop(0)
    
    def abrircajanueva(self,maxenfila,filanueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        pass
    
    
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.fila.append(cliente)
        self.enfila += 1
        pass

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1                                     #el SELF es una referencia al objeto
        self.fila.pop(0)
        pass      

    

class cliente(object):
    """clase cliente """
    def __init__(self,dni):
        """ constructor de la clase cliente """
        self.dni=dni
        self.categoria='general'
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria=categoria
        pass
  
    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
