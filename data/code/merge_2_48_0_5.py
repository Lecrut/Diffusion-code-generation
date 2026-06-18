def divide_numbers(a: float, b: float) -> None:
    if not isinstance(b, (int, float)):
        raise TypeError("Second operand must be numeric.")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    result = a / b
    import math
    if not isinstance(result, (int, float)) or math.isnan(result):
        print(f"Result is invalid: {result}")
        return
    print(f"{a} divided by {b} equals {result:.2f}")
if __name__ == '__main__':
    num1 = 45.0
    num2 = 9
    try:
        divide_numbers(num1, num2)
        test_num1 = 10
        test_num2 = 0
        print("\nTesting zero division:")
        try:
            result_test = divide_numbers(test_num1, test_num2)
        except ZeroDivisionError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {type(e).__name__}: {e}")