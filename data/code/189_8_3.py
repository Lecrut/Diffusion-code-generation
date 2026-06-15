def remove_first_occurrence(data_list, item):
    try:
        index = data_list.index(item)
        data_list.pop(index)
    except ValueError:
        pass
if __name__ == '__main__':
    my_list = [1, 2, 3, 2, 4]
    item_to_remove = 2
    print("Original list:", my_list)
    remove_first_occurrence(my_list, item_to_remove)
    print("List after removal:", my_list)
    my_list_2 = ['a', 'b', 'c', 'a', 'd']
    item_to_remove_2 = 'a'
    print("Original list 2:", my_list_2)
    remove_first_occurrence(my_list_2, item_to_remove_2)
    print("List 2 after removal:", my_list_2)
    my_list_3 = [10, 20, 30]
    item_to_remove_3 = 99
    print("Original list 3:", my_list_3)
    remove_first_occurrence(my_list_3, item_to_remove_3)
    print("List 3 after removal:", my_list_3)