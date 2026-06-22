from decimal import Decimal, InvalidOperation

def dollars_to_cents(dollars):
    try:
        dollar_value = Decimal(str(dollars))
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("Invalid input for dollar conversion")
    return int(dollar_value * 100)

if __name__ == '__main__':
    test_values = [1.23, 0.01, 100.00, 0.10, 1234.56]
    for val in test_values:
        result = dollars_to_cents(val)
        print(result)