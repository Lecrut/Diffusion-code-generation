def find_largest_data_point(*lists):
    if not lists:
        return None
    largest = None
    for current_list in lists:
        if not current_list:
            continue
        current_max = current_list[0]
        for item in current_list[1:]:
            if item > current_max:
                current_max = item
        if largest is None or current_max > largest:
            largest = current_max
    return largest

if __name__ == '__main__':
    collection_one = [10, 25, 5, 100]
    collection_two = [45, 12, 88, 3]
    collection_three = [7, 9, 200, 15]
    result = find_largest_data_point(collection_one, collection_two, collection_three)
    print(result)