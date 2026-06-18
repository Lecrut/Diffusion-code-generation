def get_element_indexable(data: list | tuple, index: int) -> any:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return data[index]
    except IndexError as e:
        print(f"Error: Index {index} is out of range for the collection. ({e})")
        raise
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    list_index = 3
    tuple_index = -1
    print(f"Element at index {list_index} in list: {get_element_indexable(sample_list, list_index)}")
    print(f"Element at index {tuple_index} in tuple: {get_element_indexable(sample_tuple, tuple_index)}")