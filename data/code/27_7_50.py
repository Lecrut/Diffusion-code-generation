def validate_numeric(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Both values must be numeric (int or float).")

def compare_inequality(a, b):
    validate_numeric(a)
    validate_numeric(b)
    return a != b

if __name__ == '__main__':
    sample_values = [42, 3.14]
    result = compare_inequality(*sample_values)
    print(result)