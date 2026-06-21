def remove_element(data, value):
    data[:] = [x for x in data if x != value]
if __name__ == '__main__':
    my_list = [1, 2, 3, 2, 4, 2, 5]
    value_to_remove = 2
    print("Original list:", my_list)
    remove_element(my_list, value_to_remove)
    print("List after removing", value_to_remove, ":", my_list)