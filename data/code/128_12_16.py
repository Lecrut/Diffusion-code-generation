def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [-1, 2, -3.5, 4.5, 0]
    for val in test_values:
        print(f"Value: {val}, Is Negative: {is_negative(val)}")