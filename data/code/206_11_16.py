def find_minimum(data):
    if not isinstance(data, list) or not all(isinstance(item, int) for item in data):
        raise ValueError("Input must be a non-empty list of integers")
    if not data:
        raise ValueError("List cannot be empty")
    
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 7]
    try:
        result = find_minimum(sample_list)
        print(result)
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        result_empty = find_minimum(empty_list)
        print(result_empty)
    except ValueError as e:
        print(e)