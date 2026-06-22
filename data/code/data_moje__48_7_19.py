def get_max_from_nested_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(get_max_from_nested_list(item))
        else:
            flat_list.append(item)
    return max(flat_list)

if __name__ == '__main__':
    data = [1, [2, 3, [4, [5, 6]], 7], 8, [9, [10, 11]]]
    result = get_max_from_nested_list(data)
    print(result)