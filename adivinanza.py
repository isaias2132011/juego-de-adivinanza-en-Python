import random

num = random.randint(1, 10)
guess = None
intentos = 0

while guess != num:
    guess = input("Adivina un número entre 1 y 10: ")
    guess = int(guess)
    intentos = intentos + 1
    
    if guess == num:
        print("¡Felicitaciones! ¡Ganaste!")
        print("Lo adivinaste en " + str(intentos) + " intentos")
    elif guess < num:
        print("El número es mayor")
    else:
        print("El número es menor")