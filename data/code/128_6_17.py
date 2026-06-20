def is_negative(value: float) -> bool:
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    return value < 0

if __name__ == '__main__':
    test_values = [-5.0, 0.0, 1.5, -0.001, 99.9]
    for val in test_values:
        result = is_negative(val)
        print(f"is_negative({val}) is {result}")