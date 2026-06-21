def remove_value(lst, value):
    return [x for x in lst if x != value]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 6, 7, 3]
    value_to_remove = 3
    filtered_list = remove_value(sample_list, value_to_remove)
    print(filtered_list)