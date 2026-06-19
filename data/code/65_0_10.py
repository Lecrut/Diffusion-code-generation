def get_element_by_position(lst, index):
    try:
        return lst[index]
    except IndexError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    valid_index = 2
    invalid_index = 10
    
    element_at_valid_index = get_element_by_position(sample_list, valid_index)
    print(f"Element at index {valid_index}: {element_at_valid_index}")
    
    element_at_invalid_index = get_element_by_position(sample_list, invalid_index)
    print(f"Element at index {invalid_index}: {element_at_invalid_index}")