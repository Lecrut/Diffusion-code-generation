def safe_divide(a: float, b: float) -> None:
    try:
        result = a / b
        print(f"{a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
if __name__ == '__main__':
    num1 = 20.5
    num2 = 4
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        safe_divide(num1, num2)