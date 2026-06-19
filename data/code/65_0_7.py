def validate_index(lst, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of bounds.")

def get_element_by_position(lst, index):
    try:
        validate_index(lst, index)
        return lst[index]
    except (TypeError, IndexError) as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    valid_index = 2
    element = get_element_by_position(sample_list, valid_index)
    print(element)

    invalid_index = 5
    element_out_of_bounds = get_element_by_position(sample_list, invalid_index)
    print(element_out_of_bounds)

    non_integer_index = "two"
    element_non_integer = get_element_by_position(sample_list, non_integer_index)
    print(element_non_integer)