def get_list_element(data_list, index):
    try:
        element = data_list[index]
        return element
    except IndexError:
        return "Error: Index out of bounds"
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 5
    result_valid = get_list_element(sample_list, valid_index)
    result_invalid = get_list_element(sample_list, invalid_index)
    print(f"List: {sample_list}")
    print(f"Attempting to retrieve element at index {valid_index}: {result_valid}")
    print(f"Attempting to retrieve element at index {invalid_index}: {result_invalid}")