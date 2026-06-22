def dollar_to_cents(dollar_amount):
    return int(abs(dollar_amount * 100))

if __name__ == '__main__':
    print(dollar_to_cents(5.99))
    print(dollar_to_cents(-2.5))
    print(dollar_to_cents(0.1))