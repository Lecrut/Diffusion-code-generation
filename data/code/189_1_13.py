def remove_element(data, value):
    data[:] = [x for x in data if x != value]

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 2, 6]
    value_to_remove = 2
    print("Original list:", my_list)
    remove_element(my_list, value_to_remove)
    print("List after removing all occurrences of", value_to_remove, ":", my_list)
    
    my_list_2 = [10, 20, 30, 40, 50]
    value_to_remove_2 = 30
    print("Original list:", my_list_2)
    remove_element(my_list_2, value_to_remove_2)
    print("List after removing", value_to_remove_2, ":", my_list_2)