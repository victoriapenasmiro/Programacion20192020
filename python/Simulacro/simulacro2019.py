## gestión de videoclub
def añadir_pelicula(lista_peliculas):
    cantidad=int(input("dame la cantidad de copias que quieres introducir: "))
    global contador_peliculas #con global estamos indicando que contador_peliculas
    global id_pelicula        #es la variable declarada en el programa principal
    
    if (contador_peliculas + cantidad <=MAX_PELICULAS):#si queda hueco para añadir las
                                 #nuevas peliculas la añado
        pelicula=[]
        contador_peliculas+=cantidad
        id_pelicula+=1
        pelicula.append(id_pelicula)
        pelicula.append(input("dame el título de la peli: "))
        pelicula.append(input("dame el director de la peli: "))
        pelicula.append(input("dame el género de la peli: "))
        pelicula.append(input("dame el año de la peli: "))            
        pelicula.append(input("dame la duración en minutos: "))
        pelicula.append(True)    #por defecto, inicialmente está disponible
        pelicula.append(cantidad) 
        pelicula.append(0) #por defecto, inicialmente no hay ninguna pelicula reservada
        lista_peliculas.append(pelicula)
    else:
        print ("No hay sitio para almacenar %d películas, ya que solo hay hueco\
para %d películas más." % (cantidad,(MAX_PELICULAS-contador_peliculas)))
    return lista_peliculas

def reservar_pelicula():
    listar_peliculas()
    id_peli=int(input("dame el id de la película que quieres reservar"))
    salir=False
    if (id_peli<=id_pelicula and id_peli>0):
        if lista_peliculas[id_peli-1][6]==True:
            print ("la película ha sido reservada")
            lista_peliculas[id_peli-1][7]-=1 #tal y como solicita el enunciado la primera peli
            if lista_peliculas[id_peli-1][7]==0: # tiene id 1, pero su posición es la 0, por tanto,
                lista_peliculas[id_peli-1][6]=False # si quiere acceder a la pelicula con id 5,
                                                    # su posición es 0
        else:
            print ("lo sentimos, la película que quieres reservar no está \
disponible")
    else:
        print ("El id de la película no existe en este videoclub")
        
def listar_peliculas():
    print ("===============================")
    print ("listado de películas")
    print ("===============================")    
    for i in lista_peliculas:#lista_peliculas es la lista que forma parte del programa principal
        mostrar_pelicula(i) #¿y por qué no usamos global? La respuesta es que solo la estamos consultando
                            #python lo interpreta de esta manera: ¿lista_peliculas existe en este
                            # procedimiento y además no le estoy asignando algo p.ej: lista_peliculas=0
                            # si hicieramos eso, crearía una nueva variable local dentro de la función
                            # leed atentamente el artículo que publiqué en el classroom
def mostrar_pelicula(peli):
        if peli[6]==True:
            disponible="Disponible" # almaceno en esta variable el literal "disponible"
        else:
            disponible="No disponible"
        print ("Id: %d Título: %s Director:%s Género: %s \
Año: %s Duración: %s minutos Estado: %s"%(peli[0],peli[1],peli[2],peli[3],\
                                          peli[4],peli[5],disponible))



def buscar_pelicula():
    opcion=menu_buscar()
    texto=input("Introduce el texto que quieres que aparezca en la búsqueda:\
")
    mostradas=0
    for i in lista_peliculas:
        if texto in i[opcion]:
            mostrar_pelicula(i)
            mostradas+=1
    if mostradas ==0:
        print ("No existe ningún título que cumpla con los criterios de búsqued\
a seleccionados")
                
def menu_buscar():
    print ("¿Qué tipo de búsqueda deseas realizar?")
    print ("1) por título")
    print ("2) por director")
    print ("3) por género")
    print ("4) por año")
    print ("5) por duracion ")
    return int(input())              
    
# =================== PROGRAMA PRINCIPAL ============================
#LISTAS
lista_peliculas=[]

# CONSTANTES
MAX_PELICULAS=3000

#VARIABLES
salir=False
contador_peliculas=0
id_pelicula=0

while salir==False:
    print ("=========================")
    print ("=   M   E   N   Ú       =")
    print ("=========================")
    print (" 1) añadir película  ")
    print (" 2) reservar película ")
    print (" 3) buscar películas ")
    print (" 4) salir")               
    print ("=========================")           
    opcion=int(input("¿Qué opción deseas? "))
    if opcion==1:
        lista_peliculas=añadir_pelicula(lista_peliculas)
    elif opcion==2:
        reservar_pelicula()
    elif opcion==3:
        buscar_pelicula()
    elif opcion==4:
        salir=True
    else:
        print ("LA OPCION INTRODUCIDA ES INCORRECTA, VUELVA A INTENTARLO ")
