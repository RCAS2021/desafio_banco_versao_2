def criar_usuario(*, contas_usuarios):

    cpf = input("Digite seu CPF: ")
    for conta_usuario in contas_usuarios:
        if conta_usuario["cpf"] == cpf:
            print("Usuário já existente")
            return
        
    nome = input("Digite o nome de usuário: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereco: ")
    contas_usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})

    print("Conta de usuário criada com sucesso!")

def criar_conta(*, contas_usuarios, numero_conta):
    cpf = input("Digite seu CPF: ")
    for conta_usuario in contas_usuarios:
        if conta_usuario["cpf"] == cpf:
            print("Conta do banco criada!")
            contas_banco.append({"contas_usuarios": conta_usuario,"agencia": "0001","numero_conta": numero_conta})
            return 
        
    print("Conta de usuário não encontrada!")

def listar_contas(*, contas_banco):
    for contas in contas_banco:
        if contas['contas_usuarios'] is not None:
            resultado = f"Nome: {contas['contas_usuarios']['nome']}, CPF: {contas['contas_usuarios']['cpf']}, Agencia: {contas['agencia']}, Numero da conta: {contas['numero_conta']}"
            print(resultado)
    
def listar_contas_usuario(*, contas_banco):
    cpf = input("Digite seu CPF: ")
    for contas in contas_banco:
        if contas['contas_usuarios'] is not None:
            if contas["contas_usuarios"]["cpf"] == cpf:
                resultado = f"Nome: {contas['contas_usuarios']['nome']}, CPF: {contas['contas_usuarios']['cpf']}, Agencia: {contas['agencia']}, Numero da conta: {contas['numero_conta']}"
                print (resultado)
            else:
                print("Conta não encontrada!")
                return    

def deletar_conta(*, contas_banco):
    conta_deletar = int(input("Digite o numero da conta: "))
    for contas in contas_banco:
        if conta_deletar == contas['numero_conta']:
            contas['contas_usuarios'] = None
            contas['numero_conta'] = [None]
            contas['agencia'] = [None]
        else:
            print("Conta não encontrada!")
            return

def depositar(saldo, extrato, /):
    deposito = float(input("\nDigite a quantidade a depositar: "))
    if deposito < 0:
        print("\nValor inválido")
    else:
        saldo += deposito
        print(f"\nDepósito efetuado com sucesso! Novo saldo:R${saldo:.2f}")
        extrato.append(f"Depósito +R${deposito:.2f}")
    return extrato, saldo

def sacar(*, extrato, saldo, numero_saques, limite_numero_saques, limite_saque):
    saque = float(input(f"\nSaldo disponível:R${saldo:.2f}\nDigite o valor a ser sacado: "))
    if saque > saldo:
        print("\nSaldo insuficiente.")
    elif saque > limite_saque:
        print("\nSaque excedeu o limite.")
    elif numero_saques >= limite_numero_saques:
        print("\nNumero de saques atingido.")
    elif saque <= 0:
        print("Valor inválido")
    else:
        saldo -= saque
        print(f"\nSaque efetuado, novo saldo:R${saldo:.2f}")
        extrato.append(f"Saque    -R${saque:.2f}")
        numero_saques +=1
    return saldo, extrato, numero_saques

def exibe_extrato(saldo, /, *, extrato):
    print("Extrato:")
    for i in extrato:
        print(i)
    print(f"Saldo:   R${saldo:.2f}")

def menu():
    menu = """
            ===========MENU==========
            1- Criar usuário
            2- Criar conta do banco
            3- Listar contas
            4- Listar contas usuário
            5- Deletar conta
            6- Depositar
            7- Sacar
            8- Extrato
            0- Sair
            =========================
            """
    return menu

saldo = 0
LIMITE_SAQUE = 500
numero_saques = 0
LIMITE_NUMERO_SAQUES = 3
extrato = []
contas_usuarios = []
contas_banco = []
numero_conta = 1


while True:
    selecionar = int(input(menu()))

    if selecionar == 1:
        criar_usuario(contas_usuarios = contas_usuarios)
    
    elif selecionar == 2:
        criar_conta(contas_usuarios = contas_usuarios, numero_conta = numero_conta)
        numero_conta += 1

    elif selecionar == 3:
        listar_contas(contas_banco = contas_banco)
    
    elif selecionar == 4:
        listar_contas_usuario(contas_banco = contas_banco)

    elif selecionar == 5:
        deletar_conta(contas_banco = contas_banco)

    elif selecionar == 6:
        extrato, saldo = depositar(saldo, extrato)
    
    elif selecionar == 7:
        saldo, extrato, numero_saques = sacar(limite_saque = LIMITE_SAQUE, limite_numero_saques = LIMITE_NUMERO_SAQUES, extrato = extrato, saldo = saldo, numero_saques = numero_saques)
    
    elif selecionar == 8:
        exibe_extrato(saldo, extrato = extrato)
    
    elif selecionar == 0:
        break
    
    else:
        print("\nOpção não existente")