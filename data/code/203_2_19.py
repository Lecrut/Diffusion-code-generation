def float_compare(value1, value2, tolerance=1e-9):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return abs(value1 - value2) <= tolerance

if __name__ == '__main__':
    result1 = float_compare(0.1 + 0.2, 0.3)
    print(f"Comparing 0.1 + 0.2 and 0.3: {result1}")