def remove_float_from_list(lst, value):
    indices = [i for i, v in enumerate(lst) if v == value]
    for i in reversed(indices):
        del lst[i]

if __name__ == '__main__':
    sample_list = [3.14, 2.71, 1.618, 2.71, 0.577]
    value_to_remove = 2.71
    remove_float_from_list(sample_list, value_to_remove)
    print(sample_list)