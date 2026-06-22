def access_list_elements(lst, indices):
    index_map = {index: value for index, value in enumerate(lst)}
    result = []
    for index in indices:
        if index in index_map:
            result.append(index_map[index])
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 6, -1]
    print(access_list_elements(sample_list, sample_indices))