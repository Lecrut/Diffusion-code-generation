def get_element_at_position(lst, index):
    try:
        return lst[index]
    except IndexError:
        return 'Index out of range'
    except TypeError:
        return 'Invalid input type'
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 3
    result = get_element_at_position(sample_list, index_to_access)
    print(result)
    invalid_index = 10
    invalid_result = get_element_at_position(sample_list, invalid_index)
    print(invalid_result)
    non_list_input = 'not a list'
    type_error_result = get_element_at_position(non_list_input, index_to_access)
    print(type_error_result)