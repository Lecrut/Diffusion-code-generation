def remove_all_occurrences(data_list, element_to_remove):
    new_list = [item for item in data_list if item != element_to_remove]
    data_list[:] = new_list
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 2, 5, 2, 6]
    element = 2
    print("Original list:", my_list)
    remove_all_occurrences(my_list, element)
    print("List after removal:", my_list)
    my_list_2 = ['a', 'b', 'c', 'a', 'd', 'a']
    element_2 = 'a'
    print("Original list 2:", my_list_2)
    remove_all_occurrences(my_list_2, element_2)
    print("List 2 after removal:", my_list_2)