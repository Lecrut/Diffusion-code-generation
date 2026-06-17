def safe_divide(a: float, b: float) -> None:
    try:
        result = a / b
        print(f"{a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError as e:
        if isinstance(a, str):
            raise
if __name__ == '__main__':
    try:
        num1 = float(10)
        num2 = 4.5
        safe_divide(num1, num2)
    except (ValueError, ZeroDivisionError):
        print("An error occurred during division.")