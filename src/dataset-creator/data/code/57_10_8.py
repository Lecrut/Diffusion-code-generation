def get_element_by_index(sequence, index):
    if not isinstance(index, int) or (index < 0 and sequence[~index] is None):
        raise IndexError("Index out of range")
    try:
        return sequence[index]
    except (TypeError, IndexError):
        raise
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd')
    list_index = 2
    tuple_index = -1
    try:
        result_list = get_element_by_index(sample_list, list_index)
        print(f"Element at index {list_index} in list: {result_list}")
        result_tuple = get_element_by_index(sample_tuple, tuple_index)
        print(f"Element at index {tuple_index} in tuple: {result_tuple}")
    except IndexError as e:
        print(f"Error accessing element: {e}")