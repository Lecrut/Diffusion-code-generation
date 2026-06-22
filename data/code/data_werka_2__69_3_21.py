def print_element_at_index(lst, index):
    try:
        if not isinstance(lst, list):
            raise TypeError("The first argument must be a list.")
        if not isinstance(index, int):
            raise TypeError("The second argument must be an integer.")
        if index < 0 or index >= len(lst):
            raise IndexError("Index is out of range.")
        print(f"Element at index {index}: {lst[index]}")
    except (TypeError, IndexError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    valid_index = 1
    invalid_index = 10
    non_list_input = "not a list"
    print_element_at_index(sample_list, valid_index)
    print_element_at_index(sample_list, invalid_index)
    print_element_at_index(non_list_input, valid_index)