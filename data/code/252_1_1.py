def compare_two_simple_quantities_now_validate(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    return a, b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 20
    try:
        normalized_data = compare_two_simple_quantities_now_validate(sample_a, sample_b)
        print(normalized_data)
    except ValueError as e:
        print(e)