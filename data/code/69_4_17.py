def validate_input(data_list, index):
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list.")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")

def get_element_at_index(data_list, index):
    validate_input(data_list, index)
    try:
        return data_list[index]
    except IndexError:
        return "Error: Index out of bounds."

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index_high = 10
    invalid_index_low = -1
    
    print("Testing valid index (2):")
    print(get_element_at_index(sample_list, valid_index))
    
    print("\nTesting valid index (first element):")
    print(get_element_at_index(sample_list, 0))
    
    print("\nTesting invalid index (too large):")
    print(get_element_at_index(sample_list, invalid_index_high))
    
    print("\nTesting invalid index (negative):")
    print(get_element_at_index(sample_list, invalid_index_low))