def get_element_at_index(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 3
    result = get_element_at_index(sample_list, index_to_access)
    print(result)
    out_of_bounds_index = 10
    result_out_of_bounds = get_element_at_index(sample_list, out_of_bounds_index)
    print(result_out_of_bounds)