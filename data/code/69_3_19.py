def print_element_at_index(data_list, index):
    try:
        element = data_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print("Error: Index out of range.")
    except TypeError:
        print("Error: Invalid input type. Please provide a list and an integer index.")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 2
    print_element_at_index(sample_list, index_to_access)

    invalid_index = 10
    print_element_at_index(sample_list, invalid_index)

    non_list_input = "not a list"
    print_element_at_index(non_list_input, index_to_access)