from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def dollars_to_cents(dollar_value):
    try:
        decimal_value = Decimal(str(dollar_value))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValueError(f'Cannot convert {dollar_value} to Decimal: {e}')
    if not decimal_value.is_finite():
        raise ValueError(f'Dollar value must be finite, got {dollar_value}')
    cents_decimal = decimal_value * 100
    cents_int = int(cents_decimal.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    return cents_int
if __name__ == '__main__':
    sample_values = ['1.00', '1.50', '0.01', '0.001', '100.999', '-5.50', 25, 0, '123.456789']
    for val in sample_values:
        result = dollars_to_cents(val)
        print(f'Dollars: {val} -> Cents: {result}')