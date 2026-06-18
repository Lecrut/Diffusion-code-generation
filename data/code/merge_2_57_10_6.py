def get_element_by_index(sequence, index):
    if not isinstance(index, int) or index < 0:
        raise IndexError("Index must be a non-negative integer.")
    try:
        return sequence[index]
    except (IndexError, TypeError):
        raise IndexError(f"Invalid access for {type(sequence).__name__}.")
if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    my_tuple = ('a', 'b', 'c')
    list_index = 2
    tuple_index = 0
    try:
        result_list = get_element_by_index(my_list, list_index)
        print(f"Element at index {list_index} in list: {result_list}")
        result_tuple = get_element_by_index(my_tuple, tuple_index)
        print(f"Element at index {tuple_index} in tuple: {result_tuple}")
    except IndexError as e:
        print(f"Error occurred: {e}")