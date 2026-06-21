def get_element_at_index(lst, index):
    return lst.get(index) if isinstance(lst, dict) else lst[index] if 0 <= index < len(lst) else None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_dict = {0: 'a', 1: 'b', 2: 'c'}
    index_to_access = 3
    result = get_element_at_index(sample_list, index_to_access)
    print(result)
    out_of_bounds_index = 10
    result_out_of_bounds = get_element_at_index(sample_list, out_of_bounds_index)
    print(result_out_of_bounds)
    dict_index_to_access = 1
    dict_result = get_element_at_index(sample_dict, dict_index_to_access)
    print(dict_result)
    dict_out_of_bounds_index = 3
    dict_result_out_of_bounds = get_element_at_index(sample_dict, dict_out_of_bounds_index)
    print(dict_result_out_of_bounds)