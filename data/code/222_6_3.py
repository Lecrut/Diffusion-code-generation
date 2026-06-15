def find_numerical_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    numerical_data = [x for x in data if isinstance(x, (int, float))]
    if not numerical_data:
        raise TypeError("No numerical data found in the list")
    minimum = numerical_data[0]
    for number in numerical_data[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    sample_list = [10, 3.5, 7, -2.1, 9, "a", 4.0]
    try:
        result = find_numerical_minimum(sample_list)
        print(result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")