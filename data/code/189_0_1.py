def remove_item_from_list(data_list, item_to_remove):
    try:
        data_list.remove(item_to_remove)
    except ValueError:
        pass
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    item1 = 3
    print("Original list:", my_list)
    remove_item_from_list(my_list, item1)
    print("List after removing", item1, ":", my_list)
    my_list2 = ['a', 'b', 'c']
    item2 = 'z'
    print("Original list:", my_list2)
    remove_item_from_list(my_list2, item2)
    print("List after attempting to remove", item2, ":", my_list2)
    my_list3 = [10, 20]
    item3 = 30
    print("Original list:", my_list3)
    remove_item_from_list(my_list3, item3)
    print("List after attempting to remove", item3, ":", my_list3)