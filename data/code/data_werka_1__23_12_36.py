def are_floats_equal(num1, num2, tolerance=1e-9):
    return abs(num1 - num2) <= tolerance

if __name__ == '__main__':
    sample_value1 = 0.1 + 0.2
    sample_value2 = 0.3
    result = are_floats_equal(sample_value1, sample_value2)
    print(result)