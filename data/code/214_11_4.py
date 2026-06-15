def find_minimum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    sample_list = [5, 12, 3, 8, 1, 9]
    result = find_minimum(sample_list)
    print(result)
    sample_tuple = (42, 100, 5, 99, 7)
    result_tuple = find_minimum(sample_tuple)
    print(result_tuple)
    sample_single = [42]
    result_single = find_minimum(sample_single)
    print(result_single)
    sample_negatives = [-10, -5, -20, -1]
    result_negatives = find_minimum(sample_negatives)
    print(result_negatives)