import random #Importamos el módulo random
from tkinter import * #importamos libreria Tkinter para la interfaz, y messagebox para que muestre ventana emergente tras victoria o derrota
from tkinter import messagebox
import unicodedata # importamos libreria unicode data y re para poder cribar respuestas casi correctas, ejemplo, que falte alguna tilde
import re

diccionario_preguntas = {
    "¿Cuál es el río más largo de la Península Ibérica?": "Tajo",
    "¿Qué país del mundo en 2023 tenía más habitantes?": "India",
    "¿Cuál es el río más largo del mundo?": "Nilo",
    "¿Cuántos mares existen en la Tierra? Por favor, introduce un número": "60",
    "¿Dónde podemos ver las auroras boreales?": "Polo Norte",
    "¿Dónde podemos ver las auroras australes?": "Polo Sur",
    "¿Qué río pasa por más paises?": "Danubio",  
    "¿Cuál es la capital de España?": "Madrid",
    "¿Cuántos países hay en el mundo? Por favor, introduce un número": "195",
    "¿Cuál es el río más largo del mundo?": "Amazonas",
    "¿Cuál es la montaña más alta de la Tierra?": "Everest",
    "¿Cuántos océanos hay en el mundo? Por favor, introduce un número": "5",
    "¿Qué país tiene la población más grande del mundo?": "China",
    "¿Cuál es el desierto más grande del mundo?": "Sahara",
    "¿Cuántos estados tiene Estados Unidos? Por favor, introduce un número": "50",
    "¿Cuál es la capital de Australia?": "Canberra",
    "¿Cuál es el lago más grande del mundo?": "Mar Caspio",
    "¿En qué continente se encuentra Egipto?": "África",
    "¿Cuál es la capital de Brasil?": "Brasilia",
    "¿Cuál es la ciudad más poblada del mundo?": "Tokio",
    "¿Cuál es la moneda oficial de la Unión Europea?": "Euro",
    "¿Cuál es el país más pequeño del mundo?": "Vaticano",
    "¿Cuál es el volcán más activo del mundo?": "Kilauea",
    "¿Cuál es la capital de Portugal?": "Lisboa",
    "¿Qué país es famoso por sus canales y bicicletas?": "Países Bajos",
    "¿Qué país tiene la forma de una bota?": "Italia",
    "¿Cuál es el río más largo de Europa?": "Volga",
    "¿Cuál es el país más pequeño de América del Sur?": "Surinam",
    "¿Qué país africano fue conocido anteriormente como Abisinia?": "Etiopía",
    "¿Cuál es el lago más grande de África?": "Lago Victoria",
    "¿Qué océano está al este de Estados Unidos?": "Océano Atlántico",
    "¿Cuál es el país más poblado de África?": "Nigeria",
    "¿Cuántas provincias tiene Canadá? Por favor, introduce un número": "10",
    "¿Cuál es la capital de Turquía?": "Ankara",
    "¿Qué país es conocido por la Torre Eiffel?": "Francia",
    "¿Cuál es el desierto más frío del mundo?": "Antártida",
    "¿Cuál es la montaña más alta de América del Norte?": "Monte McKinley",
    "¿Qué país tiene más lagos que el resto del mundo combinado?": "Canadá",
    "¿Qué país es el mayor productor de café del mundo?": "Brasil",
    "¿En qué continente se encuentra el río Nilo?": "África",
    "¿Cuál es la ciudad más grande de Australia?": "Sídney",
    "¿Cuál es la capital de Suecia?": "Estocolmo",
    "¿Qué país es famoso por sus fiordos?": "Noruega",
    "¿Cuál es el país más grande de África?": "Argelia",
    "¿Qué ciudad es conocida como la Ciudad del Viento?": "Chicago",
    "¿En qué país se encuentra el Monte Fuji?": "Japón",
    "¿Cuál es el estado más pequeño de Estados Unidos?": "Rhode Island",
    "¿Cuál es la capital de Islandia?": "Reikiavik",
    "¿Qué país tiene la ciudad de Casablanca?": "Marruecos",
    "¿Cuál es la capital de Noruega?": "Oslo",
    "¿Qué país es el mayor exportador de petróleo del mundo?": "Arabia Saudita",
    "¿Qué país de América del Sur es conocido por sus minas de esmeralda?": "Colombia",
    "¿Cuál es el lago más profundo del mundo?": "Lago Baikal",
    "¿Qué país de Europa tiene el mayor número de volcanes activos?": "Islandia",
    "¿Qué río separa México de Estados Unidos?": "Río Bravo",
    "¿Cuál es la capital de Nueva Zelanda?": "Wellington",
    "¿Qué país africano tiene la mayor cantidad de pirámides?": "Sudán",
    "¿Qué país es el más grande de la península arábiga?": "Arabia Saudita",
    "¿Cuál es la capital de Canadá?": "Ottawa",
    "¿Qué país es el único sin rectángulos en su bandera?": "Nepal",
    "¿Qué país tiene la mayor reserva de agua dulce del mundo?": "Brasil",
    "¿Cuál es la capital de Egipto?": "El Cairo",
    "¿Qué mar separa África de Europa?": "Mar Mediterráneo",
    "¿Cuál es el río más largo de Asia?": "Yangtsé",
    "¿En qué país se encuentra la montaña Aconcagua?": "Argentina",
    "¿Cuál es la capital de Grecia?": "Atenas",
    "¿Qué país europeo tiene el mayor número de habitantes?": "Alemania",
    "¿Cuál es el país más pequeño de América Central?": "El Salvador",
    "¿Qué país de Europa es conocido como el país de los mil lagos?": "Finlandia",
    "¿Cuál es la montaña más alta de África?": "Kilimanjaro",
    "¿Entre qué países se encuentra el Mar Muerto?": "Israel y Jordania",
    "¿Cuál es el canal que conecta el océano Atlántico con el océano Pacífico?": "Canal de Panamá",
    "¿Qué país es famoso por sus estructuras de piedra llamadas 'stupas'?": "Nepal",
    "¿Cuál es la capital de Austria?": "Viena",
    "¿Qué país es conocido por la Torre de Pisa?": "Italia",
    "¿Cuál es el desierto más grande de Asia?": "Desierto de Gobi",
    "¿Cuál es el océano más pequeño del mundo?": "Océano Ártico",
    "¿Cuál es el país más grande de América del Sur?": "Brasil",
    "¿Qué país es conocido por la Gran Barrera de Coral?": "Australia",
    "¿Qué país tiene como lengua oficial el portugués?": "Brasil",
    "¿En qué continente se encuentra la cordillera de los Andes?": "América del Sur",
    "¿Cuál es la capital de Dinamarca?": "Copenhague",
    "¿Qué país es el mayor productor de plata del mundo?": "Méjico",
    "¿Cuál es la capital de Escocia?": "Edimburgo",
    "¿Qué ciudad es conocida como la capital mundial del cine?": "Los Ángeles",
    "¿Cuál es la capital de Polonia?": "Varsovia",
    "¿Qué país tiene la mayor cantidad de islas en el mundo?": "Suecia",
    "¿Qué océano se encuentra al oeste de América del Sur?": "Océano Pacífico",
    "¿En qué país se encuentra Transilvania?": "Rumanía",
    "¿Cuál es la capital de Indonesia?": "Yakarta",
    "¿Qué mar se encuentra al norte de Turquía?": "Mar Negro",
    "¿Cuál es la montaña más alta de América del Sur?": "Aconcagua",
    "¿Cuál es la capital de Filipinas?": "Manila",
    "¿Qué río fluye por Viena, Bratislava, Budapest y Belgrado?": "Danubio",
    "¿Cuál es la ciudad más grande de Sudamérica?": "São Paulo",
    "¿Cuál es la capital de Irán?": "Teherán",
    "¿Cuál es el cuerpo de agua más salado del mundo?": "Mar Muerto",
    "¿Cuál es la capital de Hungría?": "Budapest",
    "¿Qué país es conocido por sus numerosos castillos y cervezas?": "República Checa",
    "¿En qué país se encuentra la región de la Toscana?": "Italia",
    "¿Qué país es el principal productor de cacao?": "Costa de Marfil",
    "¿Qué país es famoso por sus relojes y chocolate?": "Suiza",
    "¿Qué isla es compartida por tres países: Francia, Países Bajos y Reino Unido?": "San Martín",
    "¿Cuál es la capital de Ucrania?": "Kiev",
    "¿Cuál es la capital de Bélgica?": "Bruselas",
    "¿Qué río atraviesa París?": "Sena",
    "¿Qué país es conocido como la Tierra del Sol Naciente?": "Japón",
    "¿Cuál es la capital de Colombia?": "Bogotá",
    "¿En qué continente se encuentra la ciudad de Dubái?": "Asia",
    "¿Qué país es famoso por su música reggae?": "Jamaica",
    "¿Cuál es la ciudad más poblada de África?": "Lagos",
    "¿Qué país es el mayor productor de vino del mundo?": "Italia",
    "¿Cuál es la capital de Finlandia?": "Helsinki",
    "¿Qué país tiene la economía más grande de América del Sur?": "Brasil",
    "¿Cuál es la capital de la República Checa?": "Praga",
    "¿Qué país europeo es conocido por sus tapas?": "España",
    "¿Cuál es el lago más grande de América del Sur?": "Lago Titicaca",
    "¿Qué país tiene la mayor biodiversidad del mundo?": "Brasil",
    "¿Cuál es el océano más grande del mundo?": "Océano Pacífico",
    "¿Cuál es la capital de Marruecos?": "Rabat",
    "¿Qué país de Asia es el mayor exportador de electrónica?": "China",
    "¿Cuál es la capital de Gales?": "Cardiff",
    "¿Qué país es conocido por sus fiestas de Oktoberfest?": "Alemania",
    "¿Cuál es la capital de Tailandia?": "Bangkok",
    "¿Qué ciudad es conocida como la Venecia del Norte?": "San Petersburgo",
    "¿En qué país se encuentra el monte Kilimanjaro?": "Tanzania",
    "¿Qué ciudad es conocida como la Ciudad Eterna?": "Roma",
    "¿Cuál es la capital de Vietnam?": "Hanói", 
    "¿Qué estrecho separa Europa de África?": "Estrecho de Gibraltar",
    "¿Cuál es el cabo más septentrional de Europa?": "Cabo Norte",
    "¿Qué istmo conecta América del Norte con América del Sur?": "Istmo de Panamá",
    "¿Qué estrecho separa Alaska de Rusia?": "Estrecho de Bering",
    "¿Cuál es el cabo más al sur de América del Sur?": "Cabo de Hornos",
    "¿Qué estrecho conecta el mar Mediterráneo con el mar Rojo?": "Canal de Suez",
    "¿Cuál es el cabo más al norte de América del Norte?": "Cabo Barrow",
    "¿Qué estrecho separa la península arábiga de África?": "Estrecho de Bab-el-Mandeb",
    "¿Qué istmo es conocido por el canal que lo atraviesa, uniendo dos océanos?": "Istmo de Panamá",
    "¿Cuál es el cabo más al sur de África?": "Cabo Agulhas",
    "¿Qué estrecho separa las islas de Sumatra y Java?": "Estrecho de la Sonda",
    "¿Qué estrecho separa Tasmania de la Australia continental?": "Estrecho de Bass",
    "¿Cuál es el cabo situado en el extremo este de Australia?": "Cabo Byron",
    "¿Qué istmo conecta Asia con Europa?": "Istmo de Estambul",
    "¿Cuál es el cabo más oriental de América del Norte?": "Cabo Spear",
    "¿Qué estrecho separa Nueva Zelanda en dos grandes islas?": "Estrecho de Cook",
    "¿Cuál es el cabo más meridional de América del Norte?": "Cabo Sable",
    "¿Qué estrecho separa Italia de Sicilia?": "Estrecho de Mesina",
    "¿Qué istmo es conocido por su biodiversidad en Colombia?": "Istmo de Darién",
    "¿Cuál es el cabo más al oeste de África?": "Cabo Verde",
    "¿Qué estrecho separa la península de Crimea de Rusia?": "Estrecho de Kerch",
    "¿Cuál es el cabo más al este de Rusia?": "Cabo Dezhnev",
    "¿Cuál es el cabo situado en la punta norte de Escocia?": "Cabo Wrath",
    "¿Qué estrecho separa Irán de los Emiratos Árabes Unidos?": "Estrecho de Ormuz",
    "¿Qué istmo separa el mar Negro del mar de Azov?": "Istmo de Perekop",
    "¿Cuál es el cabo más al norte de África?": "Cabo Blanco",
    "¿Qué estrecho conecta el océano Atlántico con el mar del Norte?": "Estrecho de Dover",
    "¿Cuál es el cabo situado en la punta sur de la península de Baja California en México?": "Cabo San Lucas",
    "¿Qué estrecho separa Grecia de Turquía?": "Estrecho de Dardanelos"
}

class JuegoGeografía():
    
    def __init__(self,ventana,diccionario,aciertos=0,fallos=0,intentos=3,recuento=0): # metodo constructor de la clase, con sus atributos
        self.ventana = ventana # self.ventana lo necesitaremos para iniciar la ventana que se mantendrá abierta mientras dure el juego
        self.aciertos = aciertos
        self.fallos = fallos
        self.intentos=intentos
        self.recuento = recuento
        self.diccionario = diccionario
        
        self.respuesta_usuario_entry = Entry(self.ventana,font=("Helvética", 20)) # incorporamos en la interfaz caja para que el jugador introduzca la respuesta
        self.respuesta_usuario_entry.grid(row=2, column=0, padx= 60, pady= 30, sticky="w") 
        
    
    def instrucciones(self):
        
        texto = "¡Bienvenida a Preguntas y Respuestas de Geografía!\nTienes 3 intentos para responder cada pregunta correctamente.\nSi fallas 3 preguntas habrás perdido ¡Ten cuidado!\nSi aciertas 5 preguntas habrás ganado.\n!Mucha suerte! Empezamos"
        self.ventana.title("Preguntas de Geografía")
        self.ventana.geometry("1250x2000")
        #self.ventana.iconbitmap("Globo_terraqueo.ico")
        
        intro = Label(self.ventana, text=texto, bg="black", fg="white",font=("Helvética",20)) # etiqueta con el texto que muestra informacion al usuario
        intro.grid(row=0,column=0,padx=60, pady=30, sticky="nw")
        
        return texto
    
    def seleccion_pregunta(self):
        self.intentos = 3
        self.recuento += 1
        self.pregunta = random.choice(list(self.diccionario)) #Generamos una lista con las claves 
        #(preguntas) del diccionario y seleccionamos una de manera aleatoria. Lo 
        #almacenamos en la variable 'pregunta'
        
        pregunta_label = Label(self.ventana, text= f"Pregunta nº {self.recuento} => {self.pregunta}                                                                     ")
        pregunta_label.config(font=("Helvética",25), fg="darkblue") # etiqueta mostrando la pregunta seleccionada en la interfaz
        pregunta_label.grid(row=1, column=0, padx=60,sticky="w") # con grid podemos elegir donde posicionar los diferentes widgets que vamos incorporando a la interfaz
        return self.pregunta # Indicamos que lo que devuelve esta función es la variable pregunta
    
    def inicio_juego(self):
        self.instrucciones()
        
        self.seleccion_pregunta() 
        boton = Button(self.ventana, text = "Click Aquí", command=self.comprobacion_respuestazz, height= 3, width=15) 
        # generamos boton que una vez accionado por el jugador inicia el metodo comprobacion_respuesta
        boton.grid(row=3, column=0, padx=60, pady=20, sticky="w")
        
    def normalizar_texto(self,texto):
        
        # Normalizar unicode: 
        # unicodedata.normalize('NFKD', texto): Esta función descompone los caracteres acentuados en su forma básica y su tilde separada. 
        # Por ejemplo, 'á' se convierte en 'a' y un carácter de tilde separado.
        # .encode('ascii', 'ignore').decode('utf-8'): Convierte la cadena a ASCII, ignorando los caracteres que no pueden ser convertidos 
        # (como las tildes que se descompusieron anteriormente). Esto elimina las tildes y otros caracteres no ASCII.
        # .lower(): Convierte toda la cadena a minúsculas, para que las comparaciones no sean sensibles a las mayúsculas y minúsculas.
        texto_normalizado = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8').lower()
        # Eliminación de caracteres no alfanuméricos:
        # re.sub(r'[^a-z0-9\s]', '', texto_normalizado): Reemplaza cualquier carácter que no sea una letra (a-z), un número (0-9) o un espacio, 
        # con una cadena vacía. Esto elimina caracteres especiales, puntuación, etc.
        texto_normalizado = re.sub(r'[^a-z0-9\s]', '', texto_normalizado)
        # Normalización de espacios:
        # re.sub(r'\s+', ' ', texto_normalizado): Reemplaza uno o más espacios consecutivos por un solo espacio.
        # .strip(): Elimina los espacios al principio y al final de la cadena.
        texto_normalizado = re.sub(r'\s+', ' ', texto_normalizado).strip()
        return texto_normalizado

# Función para calcular la distancia de Levenshtein entre dos cadenas a y b
# la distancia es el número mínimo de operaciones neceasrias para transformar una cadena en otra.

    def distancia_levenshtein(self,a, b):
        # a es la cadena más larga. Si b es más larga que a intercambia a y b trabajando con la cadena más corta.
        if len(a) < len(b):
            return self.distancia_levenshtein(b, a)
        
        # si b está vacía, se toma la longitud de a
        if len(b) == 0:
            return len(a)
        
    # IMPORTANTE: LOS CARACTERES I Y J SON INDICES PARA ITERAR EN LAS CADENAS A Y B
    # Se inicializa el algoritmo: previous_row es la lista de enteros qeu representa la distancia entre la cadena vacía y los primeros
    # j caracteres de b. Esto genera [0,1,2,3]
    
        previous_row = range(len(b) + 1)
        # se empieza a iterar en a donde i es el índice de la posicion de la cadena a y c1 es el caracter de la cadena a:
        for i, c1 in enumerate(a):
            # empieza con i + 1 porque calcula la distancia de la subcadena i+1 de a a una cadena vacía. Fila actual.
            current_row = [i + 1]
            # para j que es el índice de la posición actual de la cadena b y c2 que es el carácter actual de la cadena b se itera sobre b:
            for j, c2 in enumerate(b):
                # insertions es el número de operaciones necesarias para insertar un carácter en a para que coincida con b.
                insertions = previous_row[j + 1] + 1
                # deletions es el número de operaciones necesarias para eliminar un carácter de a para que coincida con b.
                deletions = current_row[j] + 1
                # substitutions es el número de operaciones necesarias para sustituir un caráceter en a para que coincida con b.
                # c1 != c2 es 0 si los caracteres son iguales y 1 si son diferentes.                
                substitutions = previous_row[j] + (c1 != c2)
                # una vez realizadas las operaciones se añaden a current row (fila actual)
                current_row.append(min(insertions, deletions, substitutions))
            # al final de cada iteración sobre a, se actualiza current row para la próxima iteración.
            previous_row = current_row
        # es la distancia entre las dos cadenas.
        return previous_row[-1]

    # Función para comparar respuestas con tolerancia a errores ortográficos
    def es_respuesta_correcta(self, umbral_similitud=0.8):
        # normaliza texto eliminando tildes, convirtiendo a minúsculas y eliminando caracteres no alfabéticos
        respuesta_usuario = self.respuesta_usuario_entry.get()
        respuesta_usuario = self.normalizar_texto(respuesta_usuario)
        # se determina la longitud de la cadena más larga entre la respuesta del usuario y la correcta
        respuesta_correcta = self.diccionario[self.pregunta]
        respuesta_correcta = self.normalizar_texto(respuesta_correcta)
        # se calcula la distancia de Levenshtein entre las dos cadenas normalizadas. forma de convertir una cadena en otra.
        longitud_maxima = max(len(respuesta_usuario), len(respuesta_correcta))
        distancia = self.distancia_levenshtein(respuesta_usuario, respuesta_correcta)
        # comparación la similitud de los caracteres entre dos cadenas y aplica las operaciones necesarias para convertir una cadena en otra
        similitud = (longitud_maxima - distancia) / longitud_maxima
        # se compara la similitud de la cadena con uno predefinido (por defecto de 0.8) y si la similitud es mayor o igual al umbral, la respuesta del usuario se considera correcta:
        return similitud >= umbral_similitud
        
    def comprobacion_respuesta(self):
        self.es_respuesta_correcta()
        respuesta_usuario = self.respuesta_usuario_entry.get() 
        print(respuesta_usuario)
        
        
        if self.es_respuesta_correcta():
            self.aciertos += 1
            acierto_label = Label(self.ventana, text = f"¡Acertaste!, llevas {self.aciertos} respuestas correctas",font=("Helvética",20))
            # etiqueta mostrando al jugador que ha acerdado
            acierto_label.grid(row=4, column=0, padx= 60, pady=30,sticky="w")
            self.seleccion_pregunta() # si acierta se ejecuta el metodo self.seleccion_pregunta () para mostrar una nueva pregunta
            
            if self.aciertos == 5: #Si llegamos a 5 respuestas correctas imprimimos has ganado
                victoria_label = Label(self.ventana, text=f"¡HAS GANADO!",bg="white", fg="green", font=("Helvética", 60))
                # etiqueta mostrando al jugador que ha ganado
                victoria_label.grid(row=5,column=0, padx=60, pady=30, sticky="w")
                messagebox.showinfo("¡Ganaste!", "Enhorabuena! Has ganado el juego!")
                # ventana emergente mostrandole que ha ganado el juego
                self.ventana.destroy() # despues de message box se cierra la ventana principal
        else:
            self.intentos -= 1 #Actualizamos el número de intentos restantes quitando 1

            if self.intentos > 0: #Si aun nos quedan intentos
                fallaste_label = Label(self.ventana, text=(f"¡Fallaste! ahora te quedan => {self.intentos} intentos   "),font=("Helvética",20))
                # etiqueta mostrando que el jugador ha fallado
                fallaste_label.grid(row=4,column=0,padx=60, pady=30,sticky="w")
            else: 
                self.fallos += 1
                
                if self.fallos == 3:
                    derrota_label = Label(self.ventana, text=f"¡HAS PERDIDO!", bg="white", fg="red", font=("Helvética", 60))
                    derrota_label.grid(row=4, column=0, padx=60, pady=30, sticky="w")
                    # etiqueta mostrando que el jugador ha perdido
                    messagebox.showinfo("¡Has perdido!", "vuelve a intentarlo")
                    # ventana emergente mostrando que ha perdido y puede volver a intentarlo
                    self.ventana.destroy() # despues de messagebox se cierra la ventana principal
                    
                    
                else:
                    fallos_label = Label(self.ventana, text = f"Ya no te quedan intentos, llevas {self.fallos} fallos",font=("Helvética",20))
                    # etiqueta mostrando a jugador que ha agotado numero de intentos permitidos por preguntas y que acumula un nuevo fallo
                    fallos_label.grid(row=4, column = 0, padx=60, pady=30,sticky="w")
                    self.seleccion_pregunta() # cuando agota los intentos llamamos al metodo seleccion_pregunta mostrarle una pregunta nueva al jugador


              




            

ventana = Tk ()
jugador = JuegoGeografía(ventana,diccionario_preguntas)
jugador.inicio_juego()
ventana.mainloop()
