def print_element_at_index(data_list, index):
    try:
        element = data_list[index]
        print(element)
    except IndexError:
        print("Index out of range")
    except TypeError:
        print("Invalid index type")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_print = 2
    print_element_at_index(sample_list, index_to_print)

    invalid_index = 10
    print_element_at_index(sample_list, invalid_index)

    non_integer_index = 'a'
    print_element_at_index(sample_list, non_integer_index)