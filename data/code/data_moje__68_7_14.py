import decimal

def dollars_to_cents(dollars):
    d = decimal.Decimal(str(dollars))
    cents = int((d * 100).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))
    return cents

if __name__ == '__main__':
    print(dollars_to_cents(10.005))
    print(dollars_to_cents(1.004))
    print(dollars_to_cents(0.1))
    print(dollars_to_cents(2.555))