CENTS_PER_DOLLAR = 100
def convert_to_cents(amount):
    return int(amount * CENTS_PER_DOLLAR)
if __name__ == '__main__':
    print(convert_to_cents(99.99))
    print(convert_to_cents(0.01))