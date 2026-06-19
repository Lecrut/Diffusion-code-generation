def is_float_and_equals_pi(value):
    return isinstance(value, float) and value == 3.14

if __name__ == '__main__':
    sample_value = 3.14
    result = is_float_and_equals_pi(sample_value)
    print(result)