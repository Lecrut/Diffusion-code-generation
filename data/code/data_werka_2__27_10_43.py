def is_significantly_different(a, b, tolerance=1e-10):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both values must be either int or float.")
    return abs(a - b) > tolerance

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = is_significantly_different(value1, value2)
    print(result)