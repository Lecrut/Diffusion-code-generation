def access_list_elements(lst, indices):
    result = []
    for index in indices:
        try:
            result.append(lst[index])
        except IndexError:
            continue
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_indices = [1, 3, 5, 7]
    print(access_list_elements(sample_list, sample_indices))