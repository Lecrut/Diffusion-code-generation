def dollars_to_cents(dollar_amount):
    return abs(int(round(dollar_amount * 100)))

if __name__ == '__main__':
    print(dollars_to_cents(10.50))
    print(dollars_to_cents(-3.25))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(100))
    print(dollars_to_cents(-0.005))