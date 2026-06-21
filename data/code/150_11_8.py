def remove_value(lst, value):
    return [item for item in lst if item != value]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 2]
    value_to_remove = 2
    filtered_list = remove_value(sample_list, value_to_remove)
    print(filtered_list)