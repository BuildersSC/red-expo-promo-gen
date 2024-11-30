import random
import string

def generate_random_part():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

for _ in range(100):
    random_part = generate_random_part()
    promo_code = f"SCX-RED-2024-{random_part[:4]}-{random_part[5:]}"
    print(promo_code + "\n")
