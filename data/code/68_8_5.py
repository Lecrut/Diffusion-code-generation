def dollars_to_cents(dollar_amount):
    return abs(int(round(dollar_amount * 100)))

if __name__ == '__main__':
    print(dollars_to_cents(12.34))
    print(dollars_to_cents(-5.67))
    print(dollars_to_cents(0.0))
    print(dollars_to_cents(99.99))