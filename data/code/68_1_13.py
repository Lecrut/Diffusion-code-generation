import decimal

def dollars_to_cents(dollar_amount):
    amount = decimal.Decimal(str(dollar_amount))
    return int(amount * 100)

if __name__ == '__main__':
    print(dollars_to_cents(12.345))
    print(dollars_to_cents(0.001))
    print(dollars_to_cents(100))