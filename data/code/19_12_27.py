def is_float_equal_to_pi(value):
    return isinstance(value, float) and value == 3.14

if __name__ == '__main__':
    test_values = [3.14, 3.14159, '3.14', 3, 3.1400000000000001]
    for value in test_values:
        print(is_float_equal_to_pi(value))