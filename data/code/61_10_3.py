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
    result_valid = get_list_element(sample_list, valid_index)
    result_high = get_list_element(sample_list, invalid_index_high)
    result_low = get_list_element(sample_list, invalid_index_low)
    print(f"List: {sample_list}")
    print(f"Attempting to access index {valid_index}: {result_valid}")
    print(f"Attempting to access index {invalid_index_high}: {result_high}")
    print(f"Attempting to access index {invalid_index_low}: {result_low}")