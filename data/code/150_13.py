def remove_target_in_place(data, target):
    i = 0
    while i < len(data):
        if data[i] == target:
            data.pop(i)
        else:
            i += 1
    return data
if __name__ == '__main__':
    initial_list = [1, 5, 2, 5, 8, 5, 3]
    target_integer = 5
    result_list = remove_target_in_place(initial_list, target_integer)
    print(result_list)