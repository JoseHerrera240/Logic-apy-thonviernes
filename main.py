
nivelAgua = int(input("Digita la cantidad de agua de la represa: "))
print(f"El nivel del agua es {nivelAgua}")

if (nivelAgua < 200):
    print("No tengo agua")
elif (nivelAgua >= 200  and nivelAgua< 450):
    print("hay buen nivel de agua")
else: 
    print("El agua se va a desbordar")
