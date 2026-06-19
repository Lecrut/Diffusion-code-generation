MAX_INDEX = 10

def get_element_by_position(lst, index):
    if index < 0 or index >= len(lst) or index > MAX_INDEX:
        return None
    try:
        return lst[index]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    valid_index = 2
    element_valid = get_element_by_position(sample_list, valid_index)
    print(element_valid)
    
    out_of_bounds_index = 10
    element_out_of_bounds = get_element_by_position(sample_list, out_of_bounds_index)
    print(element_out_of_bounds)