def group_by_first_element(nested_list):
    result = {}
    for sublist in nested_list:
        key = sublist[0]
        if key not in result:
            result[key] = []
        result[key].extend(sublist[1:])
    return result

if __name__ == '__main__':
    sample_data = [
        ['a', 1, 2],
        ['b', 3],
        ['a', 4],
        ['c'],
        ['b', 5, 6]
    ]
    print(group_by_first_element(sample_data))