def find_descending_indices(data):
    indices = []
    n = len(data)
    for i in range(n - 1):
        if data[i] > data[i+1]:
            indices.append(i)
    return indices
if __name__ == '__main__':
    sample_list = [1, 3, 2, 5, 4, 7, 6]
    result = find_descending_indices(sample_list)
    print(result)