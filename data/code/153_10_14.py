def contains_integer(lst, target):
    return target in lst
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    target_value = 3
    print(contains_integer(sample_list, target_value))