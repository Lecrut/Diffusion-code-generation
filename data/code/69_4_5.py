def print_element(data_list, index):
    try:
        print(data_list[index])
    except IndexError:
        print("Error: Index out of bounds.")
    except TypeError:
        print("Error: Input must be a list and an integer index.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index_high = 10
    invalid_index_low = -1
    print("Testing valid index:")
    print_element(sample_list, valid_index)
    print("\nTesting invalid index (too high):")
    print_element(sample_list, invalid_index_high)
    print("\nTesting invalid index (too low):")
    print_element(sample_list, invalid_index_low)
    print("\nTesting with an empty list:")
    empty_list = []
    print_element(empty_list, 0)