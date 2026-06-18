def divide_numbers(a: float | int, b: float | int) -> float:
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number.")
    try:
        result = a / b
        return round(result, 10)
    except ZeroDivisionError:
        print(f"Cannot divide {a} by zero ({b}).")
        raise
if __name__ == '__main__':
    val_a = 7.5 / 3
    val_b = -42
    try:
        final_result = divide_numbers(val_a, val_b)
        print(f"Result of {val_a} divided by {val_b}: {final_result}")
        test_zero_divide = 10 / 0
    except ZeroDivisionError as e:
        print("Caught expected error:", str(e))