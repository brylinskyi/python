import random

attemp = 0

limit = 7

number = random.randint(1, 100)

print ("Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за", limit, "спроб.")

while True:
	attemp += 1

	if attemp > limit:
		print("Ви використали всі спроби.")
		break

	guess = input("Введіть ваше припущення: ")

	if not guess.isdigit():
		print("Веддіть ціле число.")
		continue

	guess = int(guess)

	if guess > number:
		print("Завелике число!")
	elif guess < number:
		print("Замале число!")
	else:
		print("Ви вгадали! Це чило", number, ".")
		break
