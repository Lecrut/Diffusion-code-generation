from decimal import Decimal, InvalidOperation

def dollars_to_cents(dollar_value):
    if isinstance(dollar_value, str):
        try:
            decimal_value = Decimal(dollar_value)
        except InvalidOperation:
            raise ValueError("Invalid dollar value string")
    elif isinstance(dollar_value, (int, float)):
        decimal_value = Decimal(str(dollar_value))
    elif isinstance(dollar_value, Decimal):
        decimal_value = dollar_value
    else:
        raise TypeError("Unsupported type for dollar value")
    
    if decimal_value < 0:
        raise ValueError("Dollar value must be non-negative")
    
    cents = decimal_value * 100
    return int(cents)

if __name__ == '__main__':
    sample_values = [
        "0.01",
        "1.00",
        "10.50",
        "0.001",
        "99.99",
        "123.456",
        Decimal("1.23"),
        1.0,
        0.5,
        "0.009"
    ]
    
    for value in sample_values:
        result = dollars_to_cents(value)
        print(result)