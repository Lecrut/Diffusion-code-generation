def remove_by_index(data_list, index):
    if 0 <= index < len(data_list):
        del data_list[index]

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    index_to_remove = 2
    print("Original list:", my_list)
    remove_by_index(my_list, index_to_remove)
    print("List after removing item at index", index_to_remove, ":", my_list)