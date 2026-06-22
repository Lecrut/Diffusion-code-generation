def compare_inequality(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both values must be numeric (int or float).")
    return a != b

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 42
    SAMPLE_VALUE_2 = 3.14
    result = compare_inequality(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    print(result)