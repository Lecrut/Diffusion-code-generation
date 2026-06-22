def flatten_and_find_minimum(data):
    flat_list = []
    for item in data:
        if isinstance(item, list):
            flat_list.extend(flatten_and_find_minimum(item))
        else:
            flat_list.append(item)
    return min(flat_list)

if __name__ == '__main__':
    nested_list1 = [5, 2, [8, 1]]
    nested_list2 = [[-10], 0, [5]]
    nested_list3 = []

    result1 = flatten_and_find_minimum(nested_list1)
    print(f"Minimum of {nested_list1}: {result1}")

    result2 = flatten_and_find_minimum(nested_list2)
    print(f"Minimum of {nested_list2}: {result2}")

    try:
        result3 = flatten_and_find_minimum(nested_list3)
    except ValueError as e:
        print(f"Caught expected error for empty list: {e}")