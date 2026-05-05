def print_element_at_index(data_list, index):
    try:
        element = data_list[index]
        print(element)
    except IndexError:
        print("Error: Index out of bounds.")
    except TypeError:
        print("Error: Input must be a list and an integer index.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Testing valid index:")
    print_element_at_index(sample_list, 2)
    print("\nTesting valid index (first element):")
    print_element_at_index(sample_list, 0)
    print("\nTesting invalid index (too large):")
    print_element_at_index(sample_list, 10)
    print("\nTesting invalid index (negative):")
    print_element_at_index(sample_list, -1)
    print("\nTesting with empty list:")
    empty_list = []
    print_element_at_index(empty_list, 0)