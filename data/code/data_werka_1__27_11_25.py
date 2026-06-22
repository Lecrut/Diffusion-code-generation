def are_values_essentially_different(a, b, tolerance=1e-10):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) > tolerance
    return a != b

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = are_values_essentially_different(value1, value2)
    print(result)