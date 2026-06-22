def find_largest_data_point(*lists):
    if not lists:
        return None
    largest = None
    for current_list in lists:
        for item in current_list:
            if largest is None or item > largest:
                largest = item
    return largest

if __name__ == '__main__':
    list_a = [3, 5, 2, 9, 1]
    list_b = [10, 4, 7, 2]
    list_c = [8, 15, 6, 11]
    result = find_largest_data_point(list_a, list_b, list_c)
    print(result)