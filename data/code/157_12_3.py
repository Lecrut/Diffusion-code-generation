def find_absolute_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for number in data[1:]:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    sample_list = [3.14, -1.5, 2.718, -10.0, 0.5, 42.0]
    result = find_absolute_minimum(sample_list)
    print(result)