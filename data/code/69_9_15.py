def access_list_elements(data_list, indices):
    result = []
    for index in indices:
        try:
            result.append(data_list[index])
        except IndexError:
            result.append(None)
    return result

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    indices_to_access = [0, 2, 4, 5, 7]
    accessed_elements = access_list_elements(sample_data, indices_to_access)
    print(accessed_elements)