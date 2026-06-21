def access_list_elements(data_list, indices):
    result = []
    for index in indices:
        try:
            result.append(data_list[index])
        except IndexError:
            continue
    return result

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 5, -1]
    print(access_list_elements(sample_data, sample_indices))