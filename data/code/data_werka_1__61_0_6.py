def fetch_element(data_list, index):
    if not isinstance(data_list, list) or not isinstance(index, int):
        return "Invalid input"
    if index < 0 or index >= len(data_list):
        return "Index out of bounds"
    return data_list[index]

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index_high = 5
    invalid_index_low = -1
    
    result_valid = fetch_element(test_list, valid_index)
    result_invalid_high = fetch_element(test_list, invalid_index_high)
    result_invalid_low = fetch_element(test_list, invalid_index_low)
    
    print(f"List: {test_list}")
    print(f"Element at index {valid_index}: {result_valid}")
    print(f"Attempt to access index {invalid_index_high}: {result_invalid_high}")
    print(f"Attempt to access index {invalid_index_low}: {result_invalid_low}")