def is_float_and_equal_to_pi(value):
    return isinstance(value, float) and value == 3.14

if __name__ == '__main__':
    sample_values = [3.14, 3.15, '3.14', 3, 3.1400000000000001]
    results = {value: is_float_and_equal_to_pi(value) for value in sample_values}
    print(results)