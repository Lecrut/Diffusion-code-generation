def compare_values(value1, value2):
    if not isinstance(value1, float) or not isinstance(value2, float):
        raise TypeError('Both inputs must be of type float.')
    import math
    if math.isclose(value1, value2, rel_tol=1e-09):
        return False
    return value1 > value2
if __name__ == '__main__':
    sample_value1 = 3.141592653589793
    sample_value2 = 3.141592653589792
    result = compare_values(sample_value1, sample_value2)
    print(result)