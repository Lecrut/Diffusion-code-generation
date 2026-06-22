from decimal import Decimal, ROUND_HALF_UP

CENTS_PER_DOLLAR = 100

def convert_dollars_to_cents(amount):
    if isinstance(amount, int):
        return amount * CENTS_PER_DOLLAR
    
    if isinstance(amount, float):
        d = Decimal(str(amount))
    elif isinstance(amount, str):
        d = Decimal(amount)
    elif isinstance(amount, Decimal):
        d = amount
    else:
        raise TypeError("Unsupported amount type")

    quantized = d.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return int(quantized * 100)

if __name__ == '__main__':
    test_values = [10.5, 0.01, 123.45, 0.29, 100, "15.99", Decimal("0.005")]
    for val in test_values:
        print(convert_dollars_to_cents(val))