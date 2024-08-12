import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Inicializa as tentativas e limita as chances
tentativas = 0
chances = 3


# Loop para permitir até 3 tentativas
while tentativas != numero_secreto and chances > 0:

    # Pede ao jogador para adivinhar o número
    tentativas = int(input(f"Adivinhe um número entre 1 e 10: "))

    # Verifica se o número digitado é maior que 10
    if tentativas < 1 or tentativas > 10:
        print("Número Inválido. Digite um número entre 1 e 10.")
        continue

    chances -= 1
    
    # Verifica se o jogador acertou
    if tentativas != numero_secreto:
        print(f"Você errou! Tente novamente. Você tem {chances} chances.")

    # Else usado para "Exibir uma mensagem de encorajamento caso o jogador acerte" conforme enunciado:
    else:
        print("Parabéns! Você acertou o número secreto! Vamos jogar novamente?")
        break

# Else usado para "Mensagem de consolo caso as 3 tentativas se esgotem sem sucesso" conforme enunciado:
else:
    print(f"Que pena! Você não acertou. O número secreto era {numero_secreto}.")