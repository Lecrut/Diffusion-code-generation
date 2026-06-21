def determine_larger(value1, value2):
    if not (isinstance(value1, (int, float)) and isinstance(value2, (int, float))):
        raise ValueError('Both values must be integers or floats')

    def find_larger(a, b):
        return a if a > b else b
    return find_larger(value1, value2)
if __name__ == '__main__':
    sample_value1 = 25.67
    sample_value2 = 89
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)