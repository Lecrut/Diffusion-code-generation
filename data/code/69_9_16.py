def validate_indices(data_list, indices):
    for index in indices:
        if not isinstance(index, int) or index < 0 or index >= len(data_list):
            return False
    return True

def access_list_elements(data_list, indices):
    if not validate_indices(data_list, indices):
        raise ValueError('Invalid indices provided.')
    result = []
    for index in indices:
        result.append(data_list[index])
    return result
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    sample_indices = [0, 2, 4, 5]
    try:
        print(access_list_elements(sample_data, sample_indices))
    except ValueError as e:
        print(e)