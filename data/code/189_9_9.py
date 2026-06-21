def reverse_remove(data_list, item_to_remove):
    for i in range(len(data_list) - 1, -1, -1):
        if data_list[i] == item_to_remove:
            del data_list[i]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 30]
    item_to_remove = 30
    print("Original list:", my_list)
    reverse_remove(my_list, item_to_remove)
    print("Resulting list:", my_list)