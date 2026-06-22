import decimal

def dollar_to_cents(dollar_amount):
    d = decimal.Decimal(str(dollar_amount))
    return int(d * 100)

if __name__ == '__main__':
    print(dollar_to_cents(10.50))
    print(dollar_to_cents(0.99))
    print(dollar_to_cents(123.4567))