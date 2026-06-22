def compare_two_simple_quantities_now_validate(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return max(a, b), min(a, b)

if __name__ == '__main__':
    sample_a = 15
    sample_b = 5
    try:
        normalized_data = compare_two_simple_quantities_now_validate(sample_a, sample_b)
        print(f"Max: {normalized_data[0]}, Min: {normalized_data[1]}")
    except ValueError as e:
        print(e)