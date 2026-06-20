def is_zero(value: float, epsilon: float = 1e-9) -> bool:
    return abs(value) < epsilon

if __name__ == '__main__':
    tolerance = 5e-10
    test_values = [0.0, tolerance, -tolerance, 1e-8, -1e-8]
    results = {val: is_zero(val, tolerance) for val in test_values}
    print(results)