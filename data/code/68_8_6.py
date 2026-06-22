def dollars_to_cents(dollar_amount):
    cents = dollar_amount * 100
    return abs(int(cents))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(-5.25))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100))