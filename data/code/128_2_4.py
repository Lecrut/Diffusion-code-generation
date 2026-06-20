def check_negativity(value):
    return value < 0

if __name__ == '__main__':
    test_values = [23.4, -17.5, 0.0, -0.123, 5.6]
    for val in test_values:
        result = check_negativity(val)
        print(f"Value: {val}, Is Negative: {result}")