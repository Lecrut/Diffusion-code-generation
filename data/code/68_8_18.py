def convert_to_cents(amount):
    return int(abs(amount) * 100)

if __name__ == '__main__':
    print(convert_to_cents(-12.34))
    print(convert_to_cents(50.05))
    print(convert_to_cents(0.01))