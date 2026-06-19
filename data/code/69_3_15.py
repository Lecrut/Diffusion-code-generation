def print_element_at_index(data, index):
    try:
        element = data[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"Error: Index {index} is out of range for the given list.")
    except TypeError:
        print("Error: The provided data is not a valid list.")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_print = 2
    print_element_at_index(sample_list, index_to_print)

    invalid_index = 10
    print_element_at_index(sample_list, invalid_index)

    non_list_data = "This is not a list"
    print_element_at_index(non_list_data, 0)