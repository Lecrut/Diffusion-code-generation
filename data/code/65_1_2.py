def get_element_by_position(data, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(data):
        raise IndexError("Index out of bounds")
    return data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"Sample List: {sample_list}")
    try:
        element1 = get_element_by_position(sample_list, 2)
        print(f"Element at index 2: {element1}")
        element_out_of_bounds = get_element_by_position(sample_list, 5)
    except IndexError as e:
        print(f"Caught expected error for index 5: {e}")
    try:
        element_negative = get_element_by_position(sample_list, -1)
    except IndexError as e:
        print(f"Caught expected error for index -1: {e}")
    try:
        element_type_error = get_element_by_position(sample_list, 1.5)
    except TypeError as e:
        print(f"Caught expected error for float index: {e}")