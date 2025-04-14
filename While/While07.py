while True:
    operacao= input('Digite uma operação: ( +, -, *, /)')

    if operacao == '+':
        numero1= int(input('Digite o primiero numero que deseja somar'))
        numero2= int(input('Diite o segundo número que deseja somar: '))

        print(f'O resultado da sua operação é: {numero1 + numero2}')
        continue

    elif operacao == '-':
        numero1= int(input('Digite o primiero numero que deseja somar'))
        numero2= int(input('Diite o segundo número que deseja somar: '))

        print(f'O resultado da sua operação é: {numero1 - numero2}')
        continue

    elif operacao == '*':
        numero1= int(input('Digite o primiero numero que deseja somar'))
        numero2= int(input('Diite o segundo número que deseja somar: '))

        print(f'O resultado da sua operação é: {numero1 * numero2}')
        continue

    elif operacao == '/':
        numero1= int(input('Digite o primiero numero que deseja somar'))
        numero2= int(input('Diite o segundo número que deseja somar: '))

        print(f'O resultado da sua operação é: {numero1 / numero2}')
        continue

    else:
        print('Inválido')