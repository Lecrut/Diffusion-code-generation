def remove_by_value(data_list, value):
    if value in data_list:
        index = data_list.index(value)
        del data_list[index]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    value_to_remove = 30
    remove_by_value(my_list, value_to_remove)
    print("List after removing", value_to_remove, ":", my_list)