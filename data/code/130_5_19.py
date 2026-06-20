def is_zero(value: float, epsilon: float = 1e-9) -> bool:
    if not isinstance(value, (int, float)) or not isinstance(epsilon, (int, float)):
        raise ValueError("Both value and epsilon must be numbers.")
    return abs(value) < epsilon

if __name__ == '__main__':
    test_values = [0.0, 1e-10, 1e-8, -1e-9, 123.456]
    for val in test_values:
        print(f"is_zero({val}) = {is_zero(val)}")