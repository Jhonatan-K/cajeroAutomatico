money = 1000

print()

while True:
    print('\t.:Bienvenido:.\n')
    print('\t.:MENU:.')
    print('1. Ingresar dinero a la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    print()
    opt = int(input("Digite una opcion de menu: "))


    if opt == 1:
        moneyInn = float(input("Cuanto dinero desea ingresar? -> "))
        money += moneyInn
        print(f'Dinero total en la cuenta: {money}')
    elif opt == 2:
        moneyOut = float(input("Cuanto dinero desea retirar? -> "))
        if moneyOut>money:
            print('No tiene esa cantidad de dinero')
        else:
            money -= moneyOut
            print(f'Dinero en la cuenta: {money}')
    elif opt == 3:
        print(f'Dinero actual: {money}')
    elif opt == 4:
        print()
        print('Gracias por utiliar su cajero automatico')
        break
    else:
        print('\tError, se equivoco de opcion de menu\n')
        
print()    
print('\tVuelva pronto\n')