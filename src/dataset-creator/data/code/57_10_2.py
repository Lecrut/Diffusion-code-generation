def get_element_by_index(sequence: tuple | list, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        element = sequence[index]
    except IndexError as e:
        print(f"Error: Index {index} is out of range. Original error: {e}")
        return
    print(f"Element at index {index}: {element}")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (5, 'hello', True)
    get_element_by_index(sample_list, 2)
    get_element_by_index(sample_tuple, -1)