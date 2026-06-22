def get_element_by_position(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = ['alpha', 'beta', 'gamma', 'delta']
    index_to_access = 1
    element_at_index = get_element_by_position(sample_list, index_to_access)
    print(element_at_index)
    
    out_of_bounds_index = 5
    element_out_of_bounds = get_element_by_position(sample_list, out_of_bounds_index)
    print(element_out_of_bounds)