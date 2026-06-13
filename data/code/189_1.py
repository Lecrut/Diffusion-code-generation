def remove_element(data, value):
    i = 0
    while i < len(data):
        if data[i] == value:
            data.pop(i)
        else:
            i += 1
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
    my_list_3 = [5, 5, 5, 5]
    value_to_remove_3 = 5
    print("Original list:", my_list_3)
    remove_element(my_list_3, value_to_remove_3)
    print("List after removing", value_to_remove_3, ":", my_list_3)
    my_list_4 = [1, 2, 3, 4]
    value_to_remove_4 = 99
    print("Original list:", my_list_4)
    remove_element(my_list_4, value_to_remove_4)
    print("List after removing", value_to_remove_4, ":", my_list_4)