def find_largest_data_point(*collections):
    if not collections:
        return None
    largest = None
    for collection in collections:
        for item in collection:
            if isinstance(item, (int, float)):
                if largest is None or item > largest:
                    largest = item
            elif isinstance(item, (list, tuple, set)):
                sub_result = find_largest_data_point(item)
                if sub_result is not None:
                    if largest is None or sub_result > largest:
                        largest = sub_result
    return largest

if __name__ == '__main__':
    list_a = [10, 25, 5, 30]
    list_b = [15, 45, 2, 100]
    list_c = [50, 20, 150, 10]
    result = find_largest_data_point(list_a, list_b, list_c)
    print(result)