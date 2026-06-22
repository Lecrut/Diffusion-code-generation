def is_float_equal_to_pi(var):
    return isinstance(var, float) and var == 3.14

if __name__ == '__main__':
    test_values = [3.14, 2.718, 3.14159, '3.14', 3, 3.1400000000000001]
    for value in test_values:
        result = is_float_equal_to_pi(value)
        print(result)