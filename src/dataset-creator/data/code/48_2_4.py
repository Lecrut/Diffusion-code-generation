def safe_divide(a: float, b: float) -> float | None:
    try:
        if b == 0:
            return None
        result = a / b
        return round(result, 10)
    except (ZeroDivisionError, TypeError):
        return None
if __name__ == '__main__':
    num1 = 25.5
    num2 = -4
    if safe_divide(num1, num2) is not None:
        print(safe_divide(num1, num2))