menu = """

[a] Cadastrar Cliente
[b] Cadastrar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_proxima_conta = 1
clientes = {}
contas = {}

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_cliente():
    cpf = input("Informe o CPF do cliente: ")
    cpf = "".join([char for char in cpf if char.isdigit()])    
    nome = input("Informe o nome do cliente: ")
    data_nascimento = input("Informe a data de nascimento do cliente: ")
    endereco = input("Informe o endereço do cliente: ")

    cpf_exists = clientes.get(cpf)

    if cpf_exists is not None:
        print(f"Operação falhou! O CPF {cpf} já existe no cadastro.")
    else:
        clientes[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
        print("Cliente cadastrado com sucesso!")

def cadastrar_conta():
    cpf = input("Informe o CPF do cliente: ")
    cpf = "".join([char for char in cpf if char.isdigit()])

    cpf_exists = clientes.get(cpf)

    if cpf_exists is None:
        print(f"Operação falhou! O CPF {cpf} não existe no cadastro.")
    else:
        global numero_proxima_conta
        contas[numero_proxima_conta] = {"agencia": "001", "cliente": cpf}
        numero_proxima_conta += 1
        print("Conta cadastrada com sucesso!")

    print(contas)
    
# --------------------------------------------------------------------------

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        result = deposito(saldo, valor, extrato)

        saldo = result[0]
        extrato = result[1]

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        result = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        saldo = result[0]
        extrato = result[1]
        numero_saques = result[2]

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "a":
        cadastrar_cliente()

    elif opcao == "b":
        cadastrar_conta()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
