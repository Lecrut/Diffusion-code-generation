def are_values_significantly_different(a, b, tolerance=1e-10):
    return abs(a - b) > tolerance

if __name__ == '__main__':
    sample_value1 = 5.0
    sample_value2 = 5.00000000000001
    difference_detected = are_values_significantly_different(sample_value1, sample_value2)
    print(difference_detected)