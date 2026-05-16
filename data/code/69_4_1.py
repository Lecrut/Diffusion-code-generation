def print_element(data_list, index):
    try:
        element = data_list[index]
        print(element)
    except IndexError:
        print("Error: Index out of bounds.")
    except TypeError:
        print("Error: Input must be a list and an integer index.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Testing valid index (2):")
    print_element(sample_list, 2)
    print("\nTesting valid index (0):")
    print_element(sample_list, 0)
    print("\nTesting invalid index (5):")
    print_element(sample_list, 5)
    print("\nTesting invalid index (-1):")
    print_element(sample_list, -1)
    print("\nTesting invalid input type (string index):")
    print_element(sample_list, "a")