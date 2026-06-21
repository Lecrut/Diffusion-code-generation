def access_list_elements(data_list, indices):
    result = []
    for index in indices:
        try:
            element = data_list[index]
            result.append(element)
        except IndexError:
            continue
    return result
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    sample_indices = [1, 3, 5, -1]
    accessed_elements = access_list_elements(sample_data, sample_indices)
    print(accessed_elements)