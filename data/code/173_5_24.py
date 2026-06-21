def group_by_first_element(data):
    grouped_data = {}
    for sublist in data:
        if sublist[0] not in grouped_data:
            grouped_data[sublist[0]] = []
        grouped_data[sublist[0]].append(sublist[1:])
    return grouped_data

if __name__ == '__main__':
    sample_data = [[1, 'a'], [2, 'b'], [1, 'c'], [3, 'd'], [2, 'e']]
    result = group_by_first_element(sample_data)
    print(result)