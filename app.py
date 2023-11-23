#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")





def jugar_ronda(opcion_jugador, opcion_oponente):
    if opcion_jugador == opcion_oponente:
        return "empate"
    elif (opcion_jugador == "rock" and opcion_oponente == "scissors") or \
         (opcion_jugador == "scissors" and opcion_oponente == "paper") or \
         (opcion_jugador == "paper" and opcion_oponente == "rock"):
        return "ganaste"
    else:
        return "perdiste"

def jugar():
    opciones = ["rock", "paper", "scissors"]
    victorias = 0
    rondas = 0

    while True:
        opcion_jugador = input("Elige rock, paper o scissors: ").lower()
        if opcion_jugador not in opciones:
            print("Opción no válida. Intenta de nuevo.")
            continue
        
        opcion_oponente = random.choice(opciones)
        print(f"El oponente eligió {opcion_oponente}.")

        resultado = jugar_ronda(opcion_jugador, opcion_oponente)
        rondas += 1

        if resultado == "ganaste":
            victorias += 1
            print("¡Ganaste esta ronda!")
        elif resultado == "perdiste":
            print("Perdiste esta ronda.")
        else:
            print("Es un empate.")

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
        if jugar_de_nuevo != "sí":
            break

    print(f"Juego terminado. Tu puntuación: {victorias} victorias en {rondas} rondas.")

if __name__ == "__main__":
    jugar()
