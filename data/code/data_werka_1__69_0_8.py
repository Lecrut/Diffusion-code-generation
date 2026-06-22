def access_elements(lst, indices):
    result = {}
    for index in indices:
        try:
            result[index] = lst[index]
        except IndexError:
            result[index] = None
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, -1, -3, 5, -6]
    accessed_elements = access_elements(sample_list, sample_indices)
    print(accessed_elements)