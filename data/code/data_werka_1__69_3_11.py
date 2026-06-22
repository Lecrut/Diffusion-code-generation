def print_element_at_index(data_list, index):
    try:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if index < 0 or index >= len(data_list):
            raise IndexError("Index is out of range.")
        print(data_list[index])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_print = 2
    print_element_at_index(sample_list, index_to_print)

    invalid_index = "five"
    print_element_at_index(sample_list, invalid_index)

    out_of_range_index = 10
    print_element_at_index(sample_list, out_of_range_index)