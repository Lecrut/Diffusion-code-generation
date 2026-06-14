def find_minimum(data):
    if not data:
        return None
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 72]
    result = find_minimum(sample_list)
    print(result)
    empty_list = []
    result_empty = find_minimum(empty_list)
    print(result_empty)