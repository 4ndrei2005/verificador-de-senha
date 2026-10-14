senha = input("Digite uma senha: ")
print("Tamanho da senha:", len(senha))

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_simbolo = False

for caractere in senha:
    if caractere.isupper():
        tem_maiuscula = True
    elif caractere.islower():
        tem_minuscula = True
    elif caractere.isdigit():
        tem_numero = True
    else:
        tem_simbolo = True

print("Tem maiúscula:", tem_maiuscula)
print("Tem minúscula:", tem_minuscula)
print("Tem número:", tem_numero)
print("Tem símbolo:", tem_simbolo)

pontos = 0

if tem_maiuscula:
    pontos = pontos + 1
if tem_minuscula:
    pontos = pontos + 1
if tem_numero:
    pontos = pontos + 1
if tem_simbolo:
    pontos = pontos + 1

print("Pontos:", pontos)

if pontos <= 1:
    print("Senha fraca")
elif pontos <= 3:
    print("Senha média")
else:
    print("Senha forte")