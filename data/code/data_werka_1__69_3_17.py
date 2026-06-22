def print_element_at_index(data, index):
    try:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if index < 0 or index >= len(data):
            raise IndexError("Index is out of range.")
        return data[index]
    except (TypeError, IndexError) as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 2
    element = print_element_at_index(sample_list, index_to_access)
    if element is not None:
        print(f"Element at index {index_to_access}: {element}")

    invalid_index = 10
    element = print_element_at_index(sample_list, invalid_index)
    if element is not None:
        print(f"Element at index {invalid_index}: {element}")

    non_integer_index = 'three'
    element = print_element_at_index(sample_list, non_integer_index)
    if element is not None:
        print(f"Element at index '{non_integer_index}': {element}")