def divide_numbers(a: float | int, b: float | int) -> float:
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number.")
    try:
        result = a / b
    except ZeroDivisionError:
        return 0.0
    return round(result, 15)
if __name__ == '__main__':
    val_a = 7.0 / 3
    val_b = 2
    result = divide_numbers(val_a, val_b)
    print(f"Result: {result}")