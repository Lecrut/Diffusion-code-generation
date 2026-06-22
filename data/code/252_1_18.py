MAX_VALUE = 100

def compare_two_simple_quantities_now_validate(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if a > MAX_VALUE or b > MAX_VALUE:
        raise ValueError("Inputs must be less than or equal to 100")
    return a, b

if __name__ == '__main__':
    sample_a = 75
    sample_b = 25
    try:
        normalized_data = compare_two_simple_quantities_now_validate(sample_a, sample_b)
        print(normalized_data)
    except ValueError as e:
        print(e)