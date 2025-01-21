import textwrap
from datetime import datetime

def menu():
    menu = """\n
    ================= MENU =================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    ==> """
    return input(textwrap.dedent(menu))



def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n### Operação falhou! O valor informado é invalido. ###")

    return saldo, extrato        

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        try:
            valor = float(input("Informe o valor do deposito: "))
        except ValueError:
            print("Erro: Não foi possivel fazer o deposito valor inválido, por favor digite um número.")
            

        if valor > 0:
            saldo += valor
            extrato += f"Déposito: R$ {valor:.2f} Em {data}\n"
        else:
            print("operação falhou valor digitado é invalido")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))      
        except ValueError:
            print("Erro: Não foi possivel fazer o saque valor inválido, por favor digite um número.")
            

        exedeu_saldo = valor > saldo
        exedeu_limite = int(valor > limite)
        exedeu_saques = numero_saque >= LIMITE_SAQUES

        if exedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif exedeu_limite:
            print("Operação falhou! O valor do saque excede o limite de R$ 500,00.")
        elif exedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")   
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f} Em {data}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}     ")
        print("==========================================")

    elif opcao == 'q':
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
