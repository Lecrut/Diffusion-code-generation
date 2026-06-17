def divide_numbers(a: float | int = 10, b: float | int = 2) -> float:
    if not isinstance(b, (int, float)) or b == 0:
        raise ValueError("Second argument must be a non-zero number.")
    try:
        result = a / b
        return round(result, 6)
    except ZeroDivisionError:
        raise
if __name__ == '__main__':
    print(divide_numbers(100, 4))