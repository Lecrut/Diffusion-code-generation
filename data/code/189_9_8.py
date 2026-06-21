def remove_value(lst, value):
    i = len(lst) - 1
    while i >= 0:
        if lst[i] == value:
            del lst[i]
        i -= 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 3]
    value_to_remove = 3
    remove_value(sample_list, value_to_remove)
    print(sample_list)