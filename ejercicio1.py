print("Hola Mundo!")

#ejercicio3
nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Ahora, ingresa tu apellido: ")
edad = input("¿cuántos años tenes?")
residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

#ejercicio4
radio = int(input("Ingrese el radio del circulo: "))
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El área del circulo es:{area} y el perimetro es:{perimetro}")

#ejercicio5
segundos = int(input("Ingrese los segundos:"))
hora = segundos / 60 / 60
print(f"Los segundos ingresados, corresponde a {hora}horas")

#ejercicio6
n = int(input("Escriba un numero:"))
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")

#ejercicio7
numero1 = int(input("Ingrese el primer numero (distinto de cero):"))
numero2 = int(input("Ingrese el segundo numero (distinto de cero):"))
if numero1 and numero2 != 0:
    suma = numero1 + numero2
    print(f"el restultado de la suma es: {suma}")
    resta = numero1 - numero2
    print(f"el resultado de la resta es: {resta}")
    multiplicacion = numero1 * numero2
    print(f"el resultado de la multiplicacion es: {multiplicacion}")
    division = numero1 / numero2
    print(f"el restultado de la division es: {division}")


#ejercicio8
peso = int(input("Ingrese su peso:"))
altura_en_cm = int(input("Ingrese su altura en cm:"))
altura_en_m = altura_en_cm / 100
imc = peso / (altura_en_m * altura_en_m)
print(f"su IMC es de: {imc}")

#ejercicio9
celsius = int(input("Ingrese la temperatura en grado celsius:"))
temperatura_en_fahrenheit = 9/5 * temperatura_en_celsius + 32
print (f"La temperatura ingresada equivalente a grados fahrenheit es: {temperatura_en_fahrenheit}")

#ejercicio10
n1 = int(input("ingrese el primer numero (distinto de cero):"))
n2 = int(input("ingrese el segundo numero (distinto de cero):"))
n3 = int(input("ingrese el tercer numero (distinto de cero):"))
if n1 and n2 and n3 != 0:
    promedio = (n1 + n2 + n3)/3
    print(f"El promedio de los 3 numeros ingresados es de: {promedio}")