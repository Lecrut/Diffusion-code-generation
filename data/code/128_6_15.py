def is_negative(num: float) -> bool:
    return num < 0

if __name__ == '__main__':
    test_values = [-3.14, 2.718, -0.001, 0.0, 100.5]
    for val in test_values:
        result = is_negative(val)
        print(f"is_negative({val}) is {result}")