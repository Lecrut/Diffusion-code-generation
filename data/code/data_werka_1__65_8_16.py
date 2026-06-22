def get_element_by_position(lst, index):
    try:
        return lst[index]
    except IndexError as e:
        raise IndexError(f"Index {index} is out of bounds for list of length {len(lst)}") from e

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    valid_index = 2
    invalid_index = 10
    negative_index = -1
    
    try:
        element_at_valid_index = get_element_by_position(sample_list, valid_index)
        print(f"Element at index {valid_index}: {element_at_valid_index}")
    except IndexError as e:
        print(e)
    
    try:
        element_at_invalid_index = get_element_by_position(sample_list, invalid_index)
        print(f"Element at index {invalid_index}: {element_at_invalid_index}")
    except IndexError as e:
        print(e)
    
    try:
        element_at_negative_index = get_element_by_position(sample_list, negative_index)
        print(f"Element at index {negative_index}: {element_at_negative_index}")
    except IndexError as e:
        print(e)