def is_float_equal_to_pi(value):
    return isinstance(value, float) and value == 3.14

if __name__ == '__main__':
    sample_value = 3.14
    result = is_float_equal_to_pi(sample_value)
    print(result)