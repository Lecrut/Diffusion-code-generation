def access_elements(data, indices):
    result = []
    for index in indices:
        if 0 <= index < len(data):
            result.append(data[index])
        else:
            result.append(None)
    return result
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 1, 10, -1]
    accessed_elements = access_elements(sample_list, sample_indices)
    print(accessed_elements)