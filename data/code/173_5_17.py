def group_data(data):
    grouped = {}
    for sublist in data:
        if not sublist:
            continue
        key = sublist[0]
        if key not in grouped:
            grouped[key] = []
        grouped[key].extend(sublist[1:])
    return grouped

if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6], [1, 7], [3, 8]]
    result = group_data(sample_data)
    print(result)