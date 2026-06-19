def print_element_at_index(lst, index):
    try:
        element = lst[index]
        print(element)
    except IndexError:
        print("Index out of range")
    except TypeError:
        print("Invalid input type")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 2
    print_element_at_index(sample_list, index_to_access)