def safe_divide(dividend: float, divisor: float) -> float:
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise ValueError('Both dividend and divisor must be numbers.')
    if divisor == 0:
        return float('inf')
    return dividend / divisor
if __name__ == '__main__':
    result = safe_divide(10.0, 2.0)
    print(result)
    result = safe_divide(5.0, 0.0)
    print(result)