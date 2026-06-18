import sys
def safe_divide(a: float, b: float) -> float | None:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be numeric.")
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Error: Division by zero. Cannot divide {a} by {b}.")
        sys.exit(1)
if __name__ == '__main__':
    num1 = 10
    num2 = 3
    try:
        result = safe_divide(num1, num2)
        print(f"Result of dividing {num1} by {num2}: {result}")
        test_num = 5.0
        test_denom = 0.0
        try:
            safe_divide(test_num, test_denom)
        except SystemExit as e:
            if e.code == 1:
                pass                                       
    except Exception as ex:
        print(f"Unexpected error occurred: {ex}")