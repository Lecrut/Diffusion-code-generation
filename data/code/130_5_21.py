def is_zero(value: float, epsilon: float = 1e-9) -> bool:
    return abs(value) < epsilon

if __name__ == '__main__':
    sample_values = [0.0, 1e-10, 1e-8, -1e-9, 123.456, 1]
    results = {val: is_zero(val) for val in sample_values}
    print(results)