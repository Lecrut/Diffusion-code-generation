def validate_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers.")
    return a, b

def check_or_condition(a, b):
    a, b = validate_numbers(a, b)
    return a > 10 or b > 10

if __name__ == '__main__':
    sample_a = 7
    sample_b = 12
    result = check_or_condition(sample_a, sample_b)
    print(result)