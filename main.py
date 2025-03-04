a = int(input("podaj liczbe:"))
lista = ["adam","bartek","kajtek","mateusz","dzyndzel","pryndzel"]
for i in range(a, len(lista)+1,a):
    print(lista[i-1])