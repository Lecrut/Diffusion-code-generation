def remove_element(data, value):
    data[:] = [x for x in data if x != value]

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    value_to_remove = 4
    print("Original list:", my_list)
    remove_element(my_list, value_to_remove)
    print("List after removing", value_to_remove, ":", my_list)

    my_list_2 = ['a', 'b', 'c', 'd', 'e', 'f']
    value_to_remove_2 = 'c'
    print("Original list:", my_list_2)
    remove_element(my_list_2, value_to_remove_2)
    print("List after removing", value_to_remove_2, ":", my_list_2)