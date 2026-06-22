def is_valid_index(data_list, index):
    return 0 <= index < len(data_list)

def get_list_element(data_list, index):
    if not is_valid_index(data_list, index):
        return "Error: Index out of bounds"
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
    result_invalid_high = get_list_element(sample_list, invalid_index_high)
    result_invalid_low = get_list_element(sample_list, invalid_index_low)
    
    print(f"List: {sample_list}")
    print(f"Element at index {valid_index}: {result_valid}")
    print(f"Attempted access at index {invalid_index_high}: {result_invalid_high}")
    print(f"Attempted access at index {invalid_index_low}: {result_invalid_low}")