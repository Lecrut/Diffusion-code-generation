def is_valid_list(data):
    return isinstance(data, list)

def remove_element(data, value):
    if not is_valid_list(data):
        raise ValueError("Data must be a list")
    
    data[:] = [x for x in data if x != value]

if __name__ == '__main__':
    my_list = [1, 2, 3, 2, 4, 2, 5]
    value_to_remove = 2
    print("Original list:", my_list)
    remove_element(my_list, value_to_remove)
    print("List after removing", value_to_remove, ":", my_list)

    my_list_2 = [10, 20, 30, 20, 40, 20]
    value_to_remove_2 = 20
    print("Original list:", my_list_2)
    remove_element(my_list_2, value_to_remove_2)
    print("List after removing", value_to_remove_2, ":", my_list_2)