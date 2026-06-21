TOLERANCE_THRESHOLD = 1e-9

def compare_floats(num1, num2, tolerance=TOLERANCE_THRESHOLD):
    return abs(num1 - num2) <= tolerance

if __name__ == '__main__':
    sample_value1 = 0.1 + 0.2
    sample_value2 = 0.3
    result = compare_floats(sample_value1, sample_value2)
    print(result)