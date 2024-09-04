# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.

valorProduto = int(input("digite o valor do seu produto! "))

valorDoImposto = (valorProduto *12) /100
valorComImposto = valorDoImposto + valorProduto

print("o valor com imposto é ",valorComImposto)

