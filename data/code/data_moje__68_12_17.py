from decimal import Decimal, ROUND_HALF_UP

def dollars_to_cents(dollars: float) -> int:
    decimal_value = Decimal(str(dollars))
    cents_decimal = decimal_value * Decimal('100')
    return int(cents_decimal.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
if __name__ == '__main__':
    test_cases = [0.0, 1.0, 0.01, 0.99, 1.23, 10.0, 123.456, -1.23, 0.1, 0.29, 100.0]
    for value in test_cases:
        print(dollars_to_cents(value))