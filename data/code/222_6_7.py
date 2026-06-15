def find_numerical_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    numerical_data = []
    for item in data:
        if isinstance(item, (int, float)):
            numerical_data.append(item)
    if not numerical_data:
        raise TypeError("No numerical data found in the list")
    minimum = numerical_data[0]
    for number in numerical_data[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    sample_data = [10, 3.5, 7, -2.1, 9.9]
    try:
        result = find_numerical_minimum(sample_data)
        print(result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    sample_data_mixed = [5, "a", 1.2, -8, None, 0]
    try:
        result_mixed = find_numerical_minimum(sample_data_mixed)
        print(result_mixed)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    sample_data_empty = []
    try:
        result_empty = find_numerical_minimum(sample_data_empty)
        print(result_empty)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")