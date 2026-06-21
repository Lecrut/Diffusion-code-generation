def find_minimum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_list = [7, 8, 3, 5, 2, 9, 1, 6]
    result = find_minimum(sample_list)
    print(result)