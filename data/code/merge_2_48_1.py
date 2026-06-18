def divide_numbers(a: float | int, b: float | int) -> float:
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number.")
    try:
        result = a / b
    except ZeroDivisionError:
        return 0.0
    if abs(result) < float('inf') and not (result == float('-infinity')) and not (result == float('+infinity')):
        rounded_result = round(result, 15)
        if rounded_result != result:
            return rounded_result
        return result
    return a / b
if __name__ == '__main__':
    sample_a = 7.0
    sample_b = 2.3456789123456789
    print(divide_numbers(sample_a, sample_b))