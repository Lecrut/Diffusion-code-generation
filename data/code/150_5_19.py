def remove_duplicates(item, lst):
    return list(set(lst) - {item})

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3]
    item_to_remove = 3
    result = remove_duplicates(item_to_remove, sample_list)
    print(result)