def get_element_by_position(lst, index):
    if index < 0 or index >= len(lst):
        return None
    return lst[index]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    valid_index = 2
    element_at_valid_index = get_element_by_position(sample_list, valid_index)
    print(element_at_valid_index)

    out_of_bounds_index = 10
    element_at_out_of_bounds_index = get_element_by_position(sample_list, out_of_bounds_index)
    print(element_at_out_of_bounds_index)