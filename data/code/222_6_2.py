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
    sample_list = [10, 3.5, -5, 8.1, "a", 2]
    try:
        result = find_numerical_minimum(sample_list)
        print(result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")