def remove_all_occurrences(data_list, item_to_remove):
    while True:
        try:
            index = data_list[::-1].index(item_to_remove)
            del data_list[-(index + 1)]
        except ValueError:
            break

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 30, 60, 70, 80, 90, 100]
    item_to_remove = 30
    print("Original list:", my_list)
    remove_all_occurrences(my_list, item_to_remove)
    print("Resulting list:", my_list)