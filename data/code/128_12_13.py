def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-2, 0, 5, -100.1, 42]
    for val in test_values:
        print(f"Value: {val}, Is Negative: {is_negative(val)}")