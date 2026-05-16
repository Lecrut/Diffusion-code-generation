def get_element_by_position(data, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    try:
        return data[index]
    except IndexError:
        raise IndexError("Index out of bounds")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"List: {sample_list}")
    try:
        result1 = get_element_by_position(sample_list, 2)
        print(f"Element at index 2: {result1}")
        result2 = get_element_by_position(sample_list, 0)
        print(f"Element at index 0: {result2}")
        result3 = get_element_by_position(sample_list, 5)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    try:
        get_element_by_position(sample_list, -1)
    except IndexError as e:
        print(f"Caught expected error for negative index: {e}")
    try:
        get_element_by_position(sample_list, "a")
    except TypeError as e:
        print(f"Caught expected error for wrong type: {e}")