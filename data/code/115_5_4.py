def calculate_quotient(numerator, denominator):
    if denominator == 0:
        raise ValueError("Division by zero is not allowed.")
    return numerator / denominator
if __name__ == '__main__':
    num1 = 10
    num2 = 2
    try:
        result = calculate_quotient(num1, num2)
        print(f"Quotient of {num1} and {num2}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    num3 = 15
    num4 = 0
    try:
        result = calculate_quotient(num3, num4)
        print(f"Quotient of {num3} and {num4}: {result}")
    except ValueError as e:
        print(f"Error: {e}")