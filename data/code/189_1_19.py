def remove_target_in_place(lst, target):
    lst[:] = [x for x in lst if x != target]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6]
    target_value = 3
    remove_target_in_place(sample_list, target_value)
    print(sample_list)