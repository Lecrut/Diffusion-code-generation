def safe_divide(a: float, b: float) -> float | None:
    try:
        if b == 0:
            return None
        result = a / b
        return round(result, 10)
    except Exception:
        return None
if __name__ == '__main__':
    first_num = 25.5
    second_num = -4
    if safe_divide(first_num, second_num):
        print(safe_divide(first_num, second_num))