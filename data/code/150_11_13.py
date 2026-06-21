def remove_value(lst, value):
    return [x for x in lst if x != value]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 2]
    value_to_remove = 2
    result = remove_value(sample_list, value_to_remove)
    print(result)