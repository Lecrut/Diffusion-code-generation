def get_element_by_position(lst, index):
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    if not isinstance(index, int):
        raise TypeError("The second argument must be an integer.")
    
    bounds = {'min': 0, 'max': len(lst) - 1}
    if index < bounds['min'] or index > bounds['max']:
        raise IndexError(f"Index {index} is out of bounds for the given list.")
    
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 5
    
    try:
        element = get_element_by_position(sample_list, valid_index)
        print(f"Element at index {valid_index}: {element}")
    except IndexError as e:
        print(e)
    
    try:
        element = get_element_by_position(sample_list, invalid_index)
        print(f"Element at index {invalid_index}: {element}")
    except IndexError as e:
        print(e)