def access_list_elements(lst, indices):
    index_map = {i: True for i in range(len(lst))}
    result = []
    for index in indices:
        if index in index_map or (index < 0 and -index <= len(lst)):
            result.append(lst[index])
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 5, 7]
    print(access_list_elements(sample_list, sample_indices))