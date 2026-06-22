def determine_larger(value1, value2):
    if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
        return max(value1, value2)
    else:
        raise ValueError('Both values must be integers or floats')
if __name__ == '__main__':
    sample_value1 = 99
    sample_value2 = 3.14159
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)
    try:
        invalid_value1 = 'string'
        invalid_value2 = 42
        print(determine_larger(invalid_value1, invalid_value2))
    except ValueError as e:
        print(e)
    try:
        another_invalid_value1 = [1, 2, 3]
        another_invalid_value2 = 5.5
        print(determine_larger(another_invalid_value1, another_invalid_value2))
    except ValueError as e:
        print(e)