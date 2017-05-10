import random
import string

x = True

while x == True:
	generated_password = ''
	password_range = range(8,17)
	password_length = random.choice(password_range)
	pool = string.ascii_letters + string.punctuation

	while len(generated_password) <= password_length:
		character_choice = random.choice(pool)
		generated_password += character_choice

	if not any(x.isupper() for x in generated_password):
		x = True
	if not any(x.islower() for x in generated_password):
		x = True
	if not any(x.isdigit() for x in generated_password):
		x = True

	print(generated_password)
	x = False