def dollars_to_cents(dollar_value):
    return int(round(dollar_value * 100))

if __name__ == '__main__':
    print(dollars_to_cents(1.005))
    print(dollars_to_cents(1.005))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(0.995))
    print(dollars_to_cents(123.456))