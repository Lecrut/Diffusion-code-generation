def convert_dollars_to_cents(dollar_amount):
    cents = int(round(abs(dollar_amount) * 100))
    return cents

if __name__ == '__main__':
    print(convert_dollars_to_cents(-12.34))
    print(convert_dollars_to_cents(5.67))
    print(convert_dollars_to_cents(0.01))