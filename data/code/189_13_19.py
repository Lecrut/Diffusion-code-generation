def remove_value(lst, value):
    return [x for x in lst if x != value]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6]
    value_to_remove = 3
    result = remove_value(sample_list, value_to_remove)
    print(result)