def soma(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    if a == 0 or b == 0:
        print("Resultado é 0 por um dos termos serem 0!!")
        return 0
    return a * b
def div(a, b):
    if b == 0:
        print("Impossivel dividir por zero")
        return None
    else:
        return a / b

operacoes = {
    "+": soma,
    "-": sub,
    "*": mult,
    "/": div,
}

historico = []
resultado = 0
prosseguir = 0
while prosseguir != 1:
    valor1 = float(input("Digite o primeiro número: "))
    op = input("Digite o operador: ")
    valor2 = float(input("Digite o segundo número: "))
    resultado_temp = operacoes[op](valor1, valor2)
    if resultado_temp is not None:
        resultado = resultado_temp
        historico.append(f"{valor1} {op} {valor2} = {resultado}")
        print("Resultado:", resultado)
        prosseguir = 1

while True:
    b = input("Digite o número (ou s para sair): \n")
    if b.lower() == "s":
        break
    b = float(b)
    a = resultado
    op = input("Digite o operador referente a conta que deseja realizar:\n"
               "|  +(soma)   ||  -(subtração) ||  *(multiplicação)  ||  /(divisão)\n")

    if op in operacoes:
        resultado_temp = operacoes[op](a, b)
        if resultado_temp is not None:
            resultado = resultado_temp
            print("Resultado: ",resultado)
            operacao_str = f"{a} {op} {b} = {resultado}"
            historico.append(operacao_str)

            print("\n******************************\n")
            print("Historico:\n")
            for i in historico:
                print(i, "\n")
    else:
        print("Operador inválido!!!")