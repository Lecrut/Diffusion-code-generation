def remove_target_in_place(data, target):
    i = 0
    while i < len(data):
        if data[i] == target:
            data.pop(i)
        else:
            i += 1
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 2, 5, 2, 6]
    target_value = 2
    print("Original list:", my_list)
    remove_target_in_place(my_list, target_value)
    print("List after removal:", my_list)