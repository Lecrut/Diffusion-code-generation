def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-3, 7, -0.5, 100, 0]
    for val in test_values:
        result = is_negative(val)
        print(f"Value: {val}, Is Negative: {result}")