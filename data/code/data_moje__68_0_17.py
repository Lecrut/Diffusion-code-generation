import decimal

def dollar_to_cents(amount: float) -> int:
    d = decimal.Decimal(str(amount))
    return int((d * 100).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))

if __name__ == '__main__':
    test_values = [10.0, 10.995, 10.994, 0.01, 100.005]
    for val in test_values:
        print(dollar_to_cents(val))