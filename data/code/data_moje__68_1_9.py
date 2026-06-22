from decimal import Decimal, InvalidOperation

def dollars_to_cents(dollar_value):
    if isinstance(dollar_value, (int, float, str)):
        try:
            decimal_value = Decimal(str(dollar_value))
        except InvalidOperation:
            raise ValueError("Invalid dollar value provided")
    elif isinstance(dollar_value, Decimal):
        decimal_value = dollar_value
    else:
        raise TypeError("Dollar value must be a number or string")

    cents = decimal_value * 100
    return int(cents)

if __name__ == '__main__':
    sample_values = [
        10.50,
        "100.99",
        Decimal("0.01"),
        0,
        -25.75,
        "1234.56"
    ]

    for value in sample_values:
        result = dollars_to_cents(value)
        print(result)