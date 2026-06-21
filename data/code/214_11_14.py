def find_minimum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            return item
    return minimum

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    result = find_minimum(sample_list)
    print(result)