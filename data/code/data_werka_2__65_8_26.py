def get_element_by_position(lst, index):
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    if not isinstance(index, int):
        raise TypeError("The second argument must be an integer.")
    try:
        return lst[index]
    except IndexError:
        raise IndexError(f"Index {index} is out of bounds for the given list.")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 7
    try:
        element = get_element_by_position(sample_list, valid_index)
        print(f"Element at index {valid_index}: {element}")
    except IndexError as e:
        print(e)

    try:
        element = get_element_by_position(sample_list, invalid_index)
        print(f"Element at index {invalid_index}: {element}")
    except IndexError as e:
        print(e)