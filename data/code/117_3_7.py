from decimal import Decimal

def validate_decimal(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float")
    return Decimal(str(value))

def calculate_monetary_difference(value1, value2):
    validated_value1 = validate_decimal(value1)
    validated_value2 = validate_decimal(value2)
    return validated_value1 - validated_value2

if __name__ == '__main__':
    amount_a = 10.50
    amount_b = 3.25
    result = calculate_monetary_difference(amount_a, amount_b)
    print(result)