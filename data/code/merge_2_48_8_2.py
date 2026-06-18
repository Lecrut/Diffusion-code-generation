import sys
def calculate_division(a: float, b: float) -> str:
    try:
        result = a / b
        return f"Result: {result:.2f}"
    except ZeroDivisionError as e:
        return f"Runtime Error: Division by zero. ({e})"
if __name__ == '__main__':
    numerator = 100.5
    denominator = 4
    output_message = calculate_division(numerator, denominator)
    print(output_message)