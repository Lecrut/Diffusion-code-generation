def divide_numbers(a: float | int, b: float | int) -> float:
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number.")
    try:
        result = a / b
    except ZeroDivisionError:
        return 0.0
    if abs(result) < float('inf') and not (result == float('-infinity')) and not (result == float('+infinity')):
        rounded_result = round(result, 15)
        return rounded_result
    return result
if __name__ == '__main__':
    val_a = 7.0 / 3.0
    val_b = -42.0
    print(divide_numbers(val_a, val_b))