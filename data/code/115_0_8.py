def safe_divide(dividend: float, divisor: float) -> float:
    if divisor == 0:
        return float('inf')
    else:
        return dividend / divisor

if __name__ == '__main__':
    result = safe_divide(10.0, 2.0)
    print(result)
    result = safe_divide(5.0, 0.0)
    print(result)