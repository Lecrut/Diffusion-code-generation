def reverse_remove(data_list, item_to_remove):
    try:
        index = data_list[::-1].index(item_to_remove)
        del data_list[-(index + 1)]
    except ValueError:
        return

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    item1 = 30
    item2 = 99
    print("Original list:", my_list)
    reverse_remove(my_list, item1)
    print("Resulting list after removing existing item (", item1, "):", my_list)
    reverse_remove(my_list, item2)
    print("Resulting list after attempting to remove non-existing item (", item2, "):", my_list)