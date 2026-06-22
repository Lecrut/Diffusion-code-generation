def compare_two_simple_quantities_now_validate(a, b):
    MIN_VALUE = 0
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if a < MIN_VALUE or b < MIN_VALUE:
        raise ValueError("Inputs must be non-negative")
    return max(a, b), min(a, b)

if __name__ == '__main__':
    sample_a = 10
    sample_b = 20
    try:
        normalized_data = compare_two_simple_quantities_now_validate(sample_a, sample_b)
        print(normalized_data)
    except ValueError as e:
        print(e)