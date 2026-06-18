def divide_numbers(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numeric types.")
    try:
        result = a / b
        import math
        if abs(result - round(result, 10)) > 1e-9 and not (math.isinf(result) or math.isnan(result)):
            return round(result, 10)
        return result
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.")
if __name__ == '__main__':
    a = 7.5
    b = 2.3
    try:
        quotient = divide_numbers(a, b)
        print(f"Result of {a} / {b}: {quotient}")
        result_zero_divide = divide_numbers(10, 0)
    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")