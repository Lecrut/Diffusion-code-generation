def is_negative(value: float) -> bool:
    return value < 0

if __name__ == '__main__':
    test_values = [-10, -3.5, 0, 2, -0.0001]
    for val in test_values:
        result = is_negative(val)
        print(f"is_negative({val}) is {result}")