from decimal import Decimal, InvalidOperation

def dollars_to_cents(dollar_value):
    if not isinstance(dollar_value, (int, float, str, Decimal)):
        raise TypeError('Input must be a number or string')
    try:
        if isinstance(dollar_value, float):
            decimal_value = Decimal(repr(dollar_value))
        elif isinstance(dollar_value, int):
            decimal_value = Decimal(dollar_value)
        elif isinstance(dollar_value, str):
            decimal_value = Decimal(dollar_value)
        else:
            decimal_value = dollar_value
    except InvalidOperation:
        raise ValueError('Invalid decimal string')
    cents_value = decimal_value * 100
    return int(cents_value)
if __name__ == '__main__':
    sample_values = [1.0, 0.5, 123.45, 0.01, 100.0, '99.99', '0.10', 1, 0]
    for value in sample_values:
        result = dollars_to_cents(value)
        print(f'Dollars: {value} -> Cents: {result}')