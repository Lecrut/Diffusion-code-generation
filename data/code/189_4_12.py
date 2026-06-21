def remove_duplicates(lst, value):
    return [x for x in lst if x != value]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 4, 3, 5]
    value_to_remove = 3
    result = remove_duplicates(sample_list, value_to_remove)
    print(result)