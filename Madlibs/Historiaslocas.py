# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga: 
# Aprende a programar con ______________.


# organizacion = "CodeAng"

# print("Aprende a programar con " + organizacion)
# print("Aprende a programar con {}". format(organizacion))
# print(f"Aprende a programar con {organizacion}") # f-string

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")

MadLibs = f"¡Programar es tan {adj}! Siempre me apasiona porque me encanta {verbo1}. ¡Aprende a {verbo2} con CodeAng y alcanza sus {sustantivo_plural}!"

print(MadLibs)