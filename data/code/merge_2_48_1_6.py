def divide_numbers(a: float | int, b: float | int) -> float:
    if not isinstance(b, (int, float)):
        raise TypeError("Both operands must be integers or floats.")
    try:
        result = a / b
        import math
        epsilon = 1e-7 if abs(result) < 1 else 1e-9 * max(abs(a), abs(b))
        return round(result, 10)
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.")
if __name__ == '__main__':
    a = 7.5
    b = 2.3
    try:
        quotient = divide_numbers(a, b)
        print(f"Result of {a} / {b}: {quotient}")
        test_zero_division = divide_numbers(10, 0)
    except (ValueError, TypeError) as e:
        print(f"Error occurred: {e}")