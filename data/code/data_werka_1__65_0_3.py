def get_element_by_position(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 3
    result = get_element_by_position(sample_list, index_to_access)
    print(result)
    index_out_of_bounds = 10
    result_out_of_bounds = get_element_by_position(sample_list, index_out_of_bounds)
    print(result_out_of_bounds)