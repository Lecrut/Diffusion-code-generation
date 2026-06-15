def find_numerical_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    numerical_data = [x for x in data if isinstance(x, (int, float))]
    if not numerical_data:
        raise TypeError("List contains no numerical data")
    minimum = numerical_data[0]
    for number in numerical_data[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    sample_data = [10, 5.5, 2, 8.1, "a", 3]
    try:
        result = find_numerical_minimum(sample_data)
        print(result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")