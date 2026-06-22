def validate_numeric(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be numeric (int or float).")

def compare_inequality(a, b):
    validate_numeric(a)
    validate_numeric(b)
    return a != b

if __name__ == '__main__':
    value1 = 7
    value2 = 3.0
    result = compare_inequality(value1, value2)
    print(result)