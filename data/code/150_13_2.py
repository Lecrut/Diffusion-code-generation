def remove_target_in_place(data, target):
    i = 0
    while i < len(data):
        if data[i] == target:
            data.pop(i)
        else:
            i += 1
    return data
if __name__ == '__main__':
    initial_list = [1, 2, 3, 4, 2, 5, 2, 6]
    target_integer = 2
    print("Initial list:", initial_list)
    modified_list = remove_target_in_place(initial_list, target_integer)
    print("List after removal:", modified_list)