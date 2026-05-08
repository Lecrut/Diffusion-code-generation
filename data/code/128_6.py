def is_strictly_less_than_zero(value: float) -> bool:
    return value < 0
if __name__ == '__main__':
    test_values = [5.0, -1.0, 0.0, -0.001, 100.5]
    for val in test_values:
        result = is_strictly_less_than_zero(val)
        print(f"is_strictly_less_than_zero({val}) is {result}")