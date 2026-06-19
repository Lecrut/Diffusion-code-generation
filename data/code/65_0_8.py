def get_element_by_position(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 3
    element = get_element_by_position(sample_list, index_to_access)
    print(element)
    index_out_of_bounds = 10
    out_of_bounds_element = get_element_by_position(sample_list, index_out_of_bounds)
    print(out_of_bounds_element)