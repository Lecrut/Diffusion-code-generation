def validate_division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise ValueError("Both dividend and divisor must be numbers")

def perform_division(dividend, divisor, decimal_places):
    return round(dividend / divisor, decimal_places)

def optimized_division(dividend, divisor, decimal_places=2):
    validate_division(dividend, divisor)
    return perform_division(dividend, divisor, decimal_places)

if __name__ == '__main__':
    dividend_large = 12345678901234567890
    divisor_small = 12345
    result = optimized_division(dividend_large, divisor_small)
    print(result)