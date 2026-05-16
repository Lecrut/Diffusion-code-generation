def safe_division(numerator, denominator):
    if denominator == 0:
        return None
    return numerator / denominator
if __name__ == '__main__':
    print(safe_division(10, 2))
    print(safe_division(10, 0))
    print(safe_division(5, 5))
    print(safe_division(-10, 2))