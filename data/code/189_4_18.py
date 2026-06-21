def remove_duplicates(lst, value):
    return [x for x in lst if x != value]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 5]
    value_to_remove = 5
    result = remove_duplicates(sample_list, value_to_remove)
    print(result)