def get_element_by_position(data_list, index):
    if not isinstance(data_list, list):
        raise TypeError("The first argument must be a list.")
    if not isinstance(index, int):
        raise TypeError("The second argument must be an integer.")
    
    try:
        return data_list[index]
    except IndexError:
        raise IndexError(f"Index {index} is out of bounds for the given list.")

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 5
    
    try:
        element = get_element_by_position(sample_data, valid_index)
        print(f"Element at index {valid_index}: {element}")
    except IndexError as e:
        print(e)
    
    try:
        element = get_element_by_position(sample_data, invalid_index)
        print(f"Element at index {invalid_index}: {element}")
    except IndexError as e:
        print(e)