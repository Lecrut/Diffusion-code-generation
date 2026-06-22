def get_element_by_position(lst, index):
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    if not isinstance(index, int):
        raise TypeError("The second argument must be an integer.")
    
    if index < 0 or index >= len(lst):
        raise IndexError(f"Index {index} is out of bounds for the given list.")
    
    return lst[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        element_at_index_2 = get_element_by_position(sample_list, 2)
        print(f"Element at index 2: {element_at_index_2}")
        
        element_at_invalid_index = get_element_by_position(sample_list, 10)
    except IndexError as e:
        print(e)