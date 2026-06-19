def print_element_at_index(data_list, index):
    try:
        element = data_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"IndexError: Index {index} is out of range for the list.")
    except TypeError:
        print("TypeError: The provided index must be an integer.")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_index = 2
    print_element_at_index(sample_list, target_index)

    another_sample_list = ['a', 'b', 'c', 'd']
    invalid_index = 10
    print_element_at_index(another_sample_list, invalid_index)

    non_integer_index = "two"
    print_element_at_index(another_sample_list, non_integer_index)