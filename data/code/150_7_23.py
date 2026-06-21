def remove_float_from_list(lst, value):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            del lst[i]
            break

if __name__ == '__main__':
    sample_list = [3.14, 2.71, 3.14, 0.57, 2.71]
    value_to_remove = 2.71
    remove_float_from_list(sample_list, value_to_remove)
    print(sample_list)