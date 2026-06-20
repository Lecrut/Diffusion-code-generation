def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_values = [1, -1, 0, 2, -2, 5.5, -5.5, 0.0]
    for val in test_values:
        print(f"is_zero({val}): {is_zero(val)}")