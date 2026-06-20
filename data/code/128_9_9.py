def is_negative(value):
    return value < 0
if __name__ == '__main__':
    test_values = [-1, -5, 0, 3]
    for val in test_values:
        print(f'Value {val} is negative: {is_negative(val)}')