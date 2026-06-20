def safe_divide(dividend: float, divisor: float) -> float:
    if divisor == 0:
        return float('inf')
    else:
        return dividend / divisor
if __name__ == '__main__':
    print(safe_divide(10.0, 2.0))
    print(safe_divide(10.0, 0.0))