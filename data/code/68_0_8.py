def dollars_to_cents(dollar_amount):
    return int(round(dollar_amount * 100))

if __name__ == '__main__':
    print(dollars_to_cents(0.10))
    print(dollars_to_cents(0.15))
    print(dollars_to_cents(1.005))
    print(dollars_to_cents(123.456))
    print(dollars_to_cents(-5.555))