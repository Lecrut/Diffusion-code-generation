def get_list_element(data_list, index):
    try:
        element = data_list[index]
        return element
    except IndexError:
        return "Error: Index out of bounds"

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index_high = 5
    invalid_index_low = -1

    results = {
        'valid': get_list_element(sample_list, valid_index),
        'invalid_high': get_list_element(sample_list, invalid_index_high),
        'invalid_low': get_list_element(sample_list, invalid_index_low)
    }

    print(f"List: {sample_list}")
    for key, value in results.items():
        print(f"Attempt to retrieve element at index {valid_index if key == 'valid' else invalid_index_high if key == 'invalid_high' else invalid_index_low}: {value}")