def group_by_first_element(data):
    grouped_data = {}
    for sublist in data:
        if len(sublist) > 0:
            key = sublist[0]
            if key not in grouped_data:
                grouped_data[key] = []
            grouped_data[key].extend(sublist[1:])
    return grouped_data

if __name__ == '__main__':
    sample_data = [[1, 'a', 2], [3, 'b'], [1, 'c', 4], [5, 'd']]
    result = group_by_first_element(sample_data)
    print(result)