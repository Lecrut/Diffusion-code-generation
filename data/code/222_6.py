def find_numerical_minimum(data):
    if not data:
        return None
    numerical_data = []
    for item in data:
        if isinstance(item, (int, float)):
            numerical_data.append(item)
    if not numerical_data:
        return None
    minimum = numerical_data[0]
    for number in numerical_data[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    sample_list = [10, 3.14, 5, -2.5, 100, "a", 0]
    result = find_numerical_minimum(sample_list)
    print(result)