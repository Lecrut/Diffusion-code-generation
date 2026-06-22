import decimal

def dollars_to_cents(amount):
    d = decimal.Decimal(str(amount))
    scaled = d * 100
    return int(scaled.to_integral_value(rounding=decimal.ROUND_HALF_UP))

if __name__ == '__main__':
    test_values = [10.50, 0.99, 100.00, 10.575, 10.5749999]
    for value in test_values:
        result = dollars_to_cents(value)
        print(f"{value} -> {result}")