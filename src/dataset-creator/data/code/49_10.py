def is_positive(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    test_values = [10.5, -3.2, 0, 4e-8]
    for val in test_values:
        result = is_positive(val)
        print(f"Value {val} is positive: {result}")