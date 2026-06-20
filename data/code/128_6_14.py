def is_negative(value: float) -> bool:
    NEGATIVE_THRESHOLD = 0.0
    return value < NEGATIVE_THRESHOLD

if __name__ == '__main__':
    test_values = [-10.5, -1.0, 0.0, 1.5, 100.5]
    for val in test_values:
        result = is_negative(val)
        print(f"Is {val} negative? {result}")