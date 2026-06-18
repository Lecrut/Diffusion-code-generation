def get_element_indexable(data: list | tuple, index: int) -> any:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return data[index]
    except IndexError as e:
        raise IndexError(f"Index {index} is out of range for the provided collection." + str(e))
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    list_index = 2
    tuple_index = -1
    try:
        result_list = get_element_indexable(sample_list, list_index)
        print(f"Element at index {list_index} in list: {result_list}")
        result_tuple = get_element_indexable(sample_tuple, tuple_index)
        print(f"Element at index {tuple_index} in tuple: {result_tuple}")
    except IndexError as e:
        print(e)