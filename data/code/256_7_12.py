def validate_input(data):
    if not data:
        raise ValueError("Input list is empty")
    for x in data:
        if not isinstance(x, (int, float)):
            raise TypeError(f"Non-integer value found: {x}")

def find_range(data):
    min_val = min(data)
    max_val = max(data)
    return max_val - min_val

if __name__ == '__main__':
    sample_data = [3.14159, 1.61803, 2.71828, 0.57721, 4.0, 1.0]
    try:
        validate_input(sample_data)
        range_result = find_range(sample_data)
        print(range_result)
    except (ValueError, TypeError) as e:
        print(e)