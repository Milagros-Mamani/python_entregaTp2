def maxJugador(lista): 
     """La funcion retorna al jugador con mas goles en la temporada"""
     max=-1
     for elem in lista: 
         if(elem["goles"]>max):
             max= elem["goles"]
             i=elem
     return i

def jugadorInfluyente(lista):
     """La funcion me devolvera el nombre del jugador mas influyente"""

     maxPromPond= lambda x, y, z : (x*1.5 + y*1.25 + z) / 3.30
     max=-1
     nom= ""
     for elem in lista:
         num=maxPromPond(elem["goles"],elem["g_evitados"],elem["asistencias"])
         if(num>max):
             max=num
             nom= elem["nombre"]
     return nom