def divide_numbers(a: float | int, b: float | int) -> float:
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number.")
    try:
        result = a / b
        return round(result, 10)
    except ZeroDivisionError:
        print(f"Warning: Division by zero for {b}.")
        return None
if __name__ == '__main__':
    val_a = 7.5
    val_b = -3
    result = divide_numbers(val_a, val_b)
    if result is not None:
        print(f"Result of dividing {val_a} by {val_b}: {result}")