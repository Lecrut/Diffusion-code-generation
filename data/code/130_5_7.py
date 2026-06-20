def is_zero(value: float, epsilon: float = 1e-9) -> bool:
    return abs(value) < epsilon

if __name__ == '__main__':
    tolerance = 1e-7
    test_values = [0.0, tolerance, -tolerance, 1e-6, -1e-6]
    results = {val: is_zero(val, tolerance) for val in test_values}
    print(results)