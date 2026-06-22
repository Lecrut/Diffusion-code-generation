def find_numerical_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    numerical_data = [x for x in data if isinstance(x, (int, float))]
    if not numerical_data:
        raise ValueError("No numerical data found in the list")
    minimum = numerical_data[0]
    for number in numerical_data[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [10, 3.14, 5, -2.5, "a", 0]
    result = find_numerical_minimum(sample_list)
    print(result)