def find_minimum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 7]
    result = find_minimum(sample_list)
    print(result)
    sample_tuple = (100, 5, 200, 1, 99)
    result_tuple = find_minimum(sample_tuple)
    print(result_tuple)
    empty_list = []
    try:
        find_minimum(empty_list)
    except ValueError as e:
        print(e)