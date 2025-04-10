def trabajar_con_archivos_texto():
    """
    Realiza operaciones de escritura y lectura en un archivo de texto.
    """

    nombre_archivo = "my_notes.txt"

    # Escritura en el archivo
    try:
        archivo_escritura = open(nombre_archivo, "w")  # Abre el archivo en modo escritura ("w")
        archivo_escritura.write("Primera nota: Recordar comprar leche.\n")
        archivo_escritura.write("Segunda nota: Llamar al dentista.\n")
        archivo_escritura.write("Tercera nota: Estudiar para el examen de Python.\n")
        archivo_escritura.close()  # Cierra el archivo después de escribir
        print(f"Se han escrito las notas en '{nombre_archivo}'.")

    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

    # Lectura del archivo
    try:
        archivo_lectura = open(nombre_archivo, "r")  # Abre el archivo en modo lectura ("r")
        print("\nContenido del archivo:")
        for linea in archivo_lectura:
            print(linea.strip())  # Imprime cada línea, eliminando espacios en blanco al principio y al final
        archivo_lectura.close()  # Cierra el archivo después de leer

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

# Llamada a la función
trabajar_con_archivos_texto()