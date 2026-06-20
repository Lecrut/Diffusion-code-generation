def is_negative(value: float) -> bool:
    return value < 0

if __name__ == '__main__':
    test_values = [-5.0, -1.0, 0.0, -0.001, 100.5]
    for val in test_values:
        result = is_negative(val)
        print(f"is_negative({val}) is {result}")