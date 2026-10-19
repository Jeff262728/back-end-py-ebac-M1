

while True:
    print("Escolha a Operação")
    print("-1 - Soma")
    print("-2 - Subtração")
    print("-3 - Multiplicação")
    print("-4 - Divisão")

    operacao = input("Escolha uma operação (1, 2, 3 ou 4): ").strip()


    if operacao in ("1", "2", "3", "4"):
       try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
       except ValueError:
            print("Erro: digite números válidos.")

       else:
        if operacao == "1":
            resultado = numero1 + numero2
            print(f"Resultado da soma: {resultado}")
        elif operacao == "2":
            resultado = numero1 - numero2
            print(f"Resultado da subtração: {resultado}")
        elif operacao == "3":
            resultado = numero1 * numero2
            print(f"Resultado da multiplicação: {resultado}")
        elif operacao == "4":
            if numero2 == 0:
                print("Erro: não é possível dividir por zero.")
            else:
                 resultado = numero1 / numero2
                 print(f"Resultado da divisão: {resultado}")   

    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 4.")

    repetir = input("Deseja fazer outra operação? (sim/não): ").strip().lower()
    if repetir not in ("sim", "s"):
        print("Obrigado por usar a calculadora. Até mais!")
        break
            