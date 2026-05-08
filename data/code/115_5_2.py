def calculate_quotient(numerator, denominator):
    if denominator == 0:
        raise ValueError("Division by zero is not allowed.")
    return numerator / denominator
if __name__ == '__main__':
    num1 = 10
    num2 = 2
    print(calculate_quotient(num1, num2))
    num3 = 15
    num4 = 3
    print(calculate_quotient(num3, num4))
    num5 = 7
    num6 = 0
    try:
        calculate_quotient(num5, num6)
    except ValueError as e:
        print(f"Error caught: {e}")