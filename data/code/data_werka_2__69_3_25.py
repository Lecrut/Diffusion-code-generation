def print_element_at_index(lst, index):
    try:
        element = lst[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"Error: Index {index} is out of range.")
    except TypeError:
        print("Error: Invalid index type. Please provide an integer.")

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    valid_index = 3
    invalid_index = 10
    non_integer_index = 'five'

    print("Valid index example:")
    print_element_at_index(sample_list, valid_index)

    print("\nInvalid index example (out of range):")
    print_element_at_index(sample_list, invalid_index)

    print("\nNon-integer index example:")
    print_element_at_index(sample_list, non_integer_index)