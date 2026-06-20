def safe_divide(num: float, denom: float) -> float:
    if denom == 0:
        return float('inf')
    else:
        return num / denom

if __name__ == '__main__':
    result = safe_divide(10.0, 2.0)
    print(result)
    result = safe_divide(5.0, 0.0)
    print(result)