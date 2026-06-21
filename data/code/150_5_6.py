def remove_duplicates(lst, item):
    return list(set(lst) - {item})

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3, 2]
    item_to_remove = 3
    result = remove_duplicates(sample_list, item_to_remove)
    print(result)