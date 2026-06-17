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
    val_a = 7.5
    val_b = 2
    try:
        final_result = divide_numbers(val_a, val_b)
        print(f"{val_a} divided by {val_b} equals {final_result}")
        test_zero_division = divide_numbers(10.5, 0)
    except ZeroDivisionError:
        pass