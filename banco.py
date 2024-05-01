

menu = '''

===== Banco do Brasil =====

Bem vindo ao banco do brasil
Qual operação você deseja
realizar?

[1] Depositar 
[2] Sacar
[3] Extrato
[0] Sair

============================
'''

LIMITE_SAQUE = 3
numero_saques = 1
saldo = 0
extrato = "" 
valor = 0
selecao ='' 

while True:

    selecao = int(input(menu))

    if selecao == 1:

        valor = float(input("Qual o valor que você deseja depositar?\n"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor de {valor:.2f}\n"
            print(f"Depósito no valor de R${valor:.2f}")

        else: 
            print("Você deve depsitar um valor maior do que zero")

    elif selecao == 2:

        valor = float(input("Quanto você deseja sacar?\n"))

        if valor < saldo and valor <= 500 and numero_saques <= LIMITE_SAQUE:
            numero_saques += 1
            saldo = saldo - valor
            extrato += f"Saque no valor de R$ {valor:.2f}\n"
            print(f'Você sacou o valor de R$ {valor:.2f}, deixando R$ {saldo} em sua conta')

        elif numero_saques >= LIMITE_SAQUE:
            print("Você excedeu o limite de saques diarios, para mais saques entre em contato com o banco para a conta premium")    

        elif valor <= saldo and valor > 500:
            print('O seu limite de saque diario é de R$ 500 reais')

        elif valor > saldo:
            print(f'Você não possui saldo suficiente, seu saldo atual é de {saldo}')

        else:
            print('Porfavor, digite um valor válido')

    elif selecao == 3:
        if extrato == "":
            print("Você não possui nenhuma movimentação")
        else:
            print(f'''Seu saldo atual é de {saldo:.2f}\n{extrato}''')

    elif selecao == 0:
        print('Obrigado por utilizar o sitema do Banco do Brasil')
        break

    else:
        print('digite um valor válido')
