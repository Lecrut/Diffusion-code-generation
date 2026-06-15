def remove_item(data_list, item_to_remove):
    try:
        data_list.remove(item_to_remove)
    except ValueError:
        pass
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    item1 = 3
    print("Original list:", my_list)
    remove_item(my_list, item1)
    print("After removing", item1, ":", my_list)
    my_list_2 = ['a', 'b', 'c']
    item2 = 'z'
    print("Original list:", my_list_2)
    remove_item(my_list_2, item2)
    print("After trying to remove", item2, ":", my_list_2)
    my_list_3 = [10, 20, 30]
    item3 = 50
    print("Original list:", my_list_3)
    remove_item(my_list_3, item3)
    print("After trying to remove", item3, ":", my_list_3)