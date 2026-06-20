def access_list_elements(data_list, indices):
    result = []
    for index in indices:
        try:
            result.append(data_list[index])
        except IndexError:
            continue
    return result

if __name__ == '__main__':
    sample_data = list(range(1000))
    sample_indices = [50, 200, 999, 1001]
    print(access_list_elements(sample_data, sample_indices))