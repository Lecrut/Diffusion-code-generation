def get_element_by_index(sequence, index):
    if not isinstance(index, int) or index < 0:
        raise IndexError("Index must be a non-negative integer.")
    try:
        return sequence[index]
    except (IndexError, TypeError):
        raise IndexError(f"Sequence is too small to access at index {index}.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    list_index = 3
    tuple_index = 1
    try:
        result_list = get_element_by_index(sample_list, list_index)
        print(f"Element from list at index {list_index}: {result_list}")
        result_tuple = get_element_by_index(sample_tuple, tuple_index)
        print(f"Element from tuple at index {tuple_index}: {result_tuple}")
    except IndexError as e:
        print(f"Error occurred: {e}")