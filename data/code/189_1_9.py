def remove_element(data, value):
    return [item for item in data if item != value]

if __name__ == '__main__':
    my_list = [1, 2, 3, 2, 4, 2, 5]
    value_to_remove = 2
    print("Original list:", my_list)
    new_list = remove_element(my_list, value_to_remove)
    print("List after removing", value_to_remove, ":", new_list)
    
    my_list_2 = [10, 20, 30, 20, 40, 20]
    value_to_remove_2 = 20
    print("Original list:", my_list_2)
    new_list_2 = remove_element(my_list_2, value_to_remove_2)
    print("List after removing", value_to_remove_2, ":", new_list_2)