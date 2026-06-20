def is_zero(value):
    return value == 0
if __name__ == '__main__':
    test_values = [0, 5, -3, 0.0, 100]
    for val in test_values:
        print(f'Value: {val}, Is Zero: {is_zero(val)}')