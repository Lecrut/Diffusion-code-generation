def print_element_at_index(data_list, index):
    try:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if index < 0 or index >= len(data_list):
            raise IndexError("Index out of range.")
        print(data_list[index])
    except (TypeError, IndexError) as e:
        print(e)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_print = 2
    print_element_at_index(sample_list, index_to_print)
    
    invalid_index = 10
    print_element_at_index(sample_list, invalid_index)
    
    non_integer_index = 'a'
    print_element_at_index(sample_list, non_integer_index)