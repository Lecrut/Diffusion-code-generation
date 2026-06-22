def float_to_cents(amount):
    return int(amount * 100 + 0.5) if amount >= 0 else int(amount * 100 - 0.5)

if __name__ == '__main__':
    print(float_to_cents(10.99))
    print(float_to_cents(10.995))
    print(float_to_cents(-10.99))
    print(float_to_cents(0.0))