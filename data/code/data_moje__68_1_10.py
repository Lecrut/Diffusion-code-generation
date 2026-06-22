from decimal import Decimal, InvalidOperation

def convert_dollars_to_cents(dollar_value):
    if isinstance(dollar_value, str):
        try:
            decimal_val = Decimal(dollar_value)
        except InvalidOperation:
            raise ValueError("Invalid dollar value provided")
    elif isinstance(dollar_value, (int, float, Decimal)):
        decimal_val = Decimal(str(dollar_value))
    else:
        raise TypeError("Unsupported input type")
    
    if decimal_val < 0:
        raise ValueError("Dollar value cannot be negative")
    
    cents = (decimal_val * 100).quantize(Decimal('1'))
    return int(cents)

if __name__ == '__main__':
    test_values = [10.5, 100, "50.25", "0.99", 1000.001, -1]
    for val in test_values:
        try:
            result = convert_dollars_to_cents(val)
            print(f"{val} -> {result} cents")
        except ValueError as e:
            print(f"{val} -> Error: {e}")
        except TypeError as e:
            print(f"{val} -> Error: {e}")