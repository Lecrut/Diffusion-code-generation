def find_inequality_indices(data):
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    inequality_indices = []
    for i in range(len(data) - 1):
        if data[i] != data[i + 1]:
            inequality_indices.append((i, data[i], data[i + 1]))
    return inequality_indices
if __name__ == '__main__':
    sample_data = [1, 'apple', [2, 3], {'a': 4}, 5.5]
    result = find_inequality_indices(sample_data)
    print(result)