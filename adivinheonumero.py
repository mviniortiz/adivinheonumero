import random


def guess(x):
	random_number = random.randint(1, x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Digite um numero entre 1 e {x}: '))
		print(guess)
		if guess < random_number:
			print("O número é menor, tente novamente!")
		elif guess > random_number:
			print("O numero é maior, tente novamente!")

	print(f'Parabéns, você acertou o número {random_number} corretamente!')


def computer_guess(x):
	low = 1
	high = x
	feedback = ''
	while feedback != 'c' and low != high:

		guess = random.randint(low, high)
		feedback = input(f'O {guess} é maior (M), menor (m), ou correto (C)?? ').lower()
		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1

	print(f"Isso ai, o computador acertou o número {guess} corretamente! ")


computer_guess(314)

guess(314)