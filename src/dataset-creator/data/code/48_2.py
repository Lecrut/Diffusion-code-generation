def safe_divide(a: float, b: float) -> None:
    try:
        result = a / b
        print(f"{a} divided by {b} is {result}")
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {e}")
if __name__ == '__main__':
    num1 = 20
    num2 = 4
    safe_divide(num1, num2)