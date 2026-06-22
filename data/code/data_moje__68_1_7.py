import decimal
from decimal import Decimal, InvalidOperation

def convert_dollars_to_cents(dollar_value):
    try:
        if isinstance(dollar_value, float):
            if dollar_value != dollar_value:
                raise ValueError("NaN values are not allowed")
            if dollar_value == float('inf') or dollar_value == float('-inf'):
                raise ValueError("Infinite values are not allowed")
            decimal_value = Decimal(str(dollar_value))
        elif isinstance(dollar_value, Decimal):
            decimal_value = dollar_value
        elif isinstance(dollar_value, str):
            decimal_value = Decimal(dollar_value)
        elif isinstance(dollar_value, int):
            decimal_value = Decimal(dollar_value)
        else:
            raise TypeError("Unsupported type for dollar_value")
        
        cents = decimal_value * Decimal('100')
        cents = cents.quantize(Decimal('1'), rounding=decimal.ROUND_HALF_UP)
        return int(cents)
    except InvalidOperation:
        raise ValueError("Invalid number format")
    except decimal.InvalidOperation:
        raise ValueError("Invalid number format")

if __name__ == '__main__':
    test_values = [10.50, 0.01, 100.00, "5.255", 20, "0.005"]
    for value in test_values:
        result = convert_dollars_to_cents(value)
        print(f"{value} dollars is {result} cents")