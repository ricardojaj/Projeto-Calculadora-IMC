try:
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite seu altura: "))
    calculoImc = peso / (altura ** 2)

    if calculoImc < 18.5:
        print(f'Seu imc: {calculoImc:.1f} | Abaixo do peso!')
    elif calculoImc >= 18.5 and calculoImc <= 24.9:
        print(f'Seu imc: {calculoImc:.1f} | Peso normal!')
    elif calculoImc >= 25 and calculoImc <= 29.9:
        print(f'Seu imc: {calculoImc:.1f} | Sobrepeso!')
    elif calculoImc >= 30 and calculoImc <= 34.9:
        print(f'Seu imc: {calculoImc:.1f} | Obesidade Grau 1!')
    elif calculoImc >= 35 and calculoImc <= 39.9:
        print(f'Seu imc: {calculoImc:.1f} | Obesidade Grau 2!')
    else:
        print(f'Seu imc: {calculoImc:.1f} | Obesidade Grau 3!')

except ValueError:
    print("Valor informado é invalido!")