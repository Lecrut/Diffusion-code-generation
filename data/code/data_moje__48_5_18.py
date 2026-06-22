def find_largest_across_lists(*lists):
    if not lists:
        return None
    max_value = None
    for collection in lists:
        for item in collection:
            if max_value is None or item > max_value:
                max_value = item
    return max_value

if __name__ == '__main__':
    data_set_1 = [3, 7, 2, 19, 5]
    data_set_2 = [10, 4, 25, 1, 8]
    data_set_3 = [12, 30, 9, 14, 21]
    data_set_4 = [6, 3, 1, 4, 5]
    result = find_largest_across_lists(data_set_1, data_set_2, data_set_3, data_set_4)
    print(result)