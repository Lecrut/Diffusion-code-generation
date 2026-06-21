def group_by_first_element(nested_list):
    result = {}
    for sublist in nested_list:
        if sublist[0] not in result:
            result[sublist[0]] = []
        result[sublist[0]].append(sublist[1:])
    return result

if __name__ == '__main__':
    sample_data = [
        ['apple', 1],
        ['banana', 2],
        ['apple', 3],
        ['orange', 4],
        ['banana', 5]
    ]
    grouped_data = group_by_first_element(sample_data)
    print(grouped_data)