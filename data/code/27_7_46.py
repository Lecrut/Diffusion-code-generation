def is_not_equal(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both values must be numeric (int or float).")
    return a != b

if __name__ == '__main__':
    sample_values = [42, 3.14]
    result = is_not_equal(sample_values[0], sample_values[1])
    print(result)