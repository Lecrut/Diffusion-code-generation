def get_element_by_position(data, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(data):
        raise IndexError("Index out of bounds")
    return data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"List: {sample_list}")
    try:
        result1 = get_element_by_position(sample_list, 2)
        print(f"Element at index 2: {result1}")
        result2 = get_element_by_position(sample_list, 0)
        print(f"Element at index 0: {result2}")
        result3 = get_element_by_position(sample_list, 4)
        print(f"Element at index 4: {result3}")
        result_error_high = get_element_by_position(sample_list, 5)
    except IndexError as e:
        print(f"Caught expected error for index 5: {e}")
    try:
        result_error_low = get_element_by_position(sample_list, -1)
    except IndexError as e:
        print(f"Caught expected error for index -1: {e}")
    try:
        result_error_type = get_element_by_position(sample_list, 1.5)
    except TypeError as e:
        print(f"Caught expected error for non-integer index: {e}")