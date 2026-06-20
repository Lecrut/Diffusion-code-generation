def safe_divide(a: float, b: float) -> float:
    if b == 0:
        return float('inf')
    else:
        return a / b

if __name__ == '__main__':
    result = safe_divide(10.0, 2.0)
    print(result)
    result = safe_divide(5.0, 0.0)
    print(result)