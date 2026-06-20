from decimal import Decimal

def validate_monetary_value(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Invalid monetary value type")
    return Decimal(str(value))

def calculate_monetary_difference(value1, value2):
    value1 = validate_monetary_value(value1)
    value2 = validate_monetary_value(value2)
    return value1 - value2

if __name__ == '__main__':
    amount_a = 10.50
    amount_b = 3.25
    result = calculate_monetary_difference(amount_a, amount_b)
    print(result)