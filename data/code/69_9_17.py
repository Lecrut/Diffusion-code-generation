def access_list_elements(data_list, indices):
    result = []
    for index in indices:
        try:
            result.append(data_list[index])
        except IndexError:
            result.append(None)
    return result

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    sample_indices = [1, 3, 5, -2]
    accessed_elements = access_list_elements(sample_data, sample_indices)
    print(accessed_elements)