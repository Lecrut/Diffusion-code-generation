def remove_duplicates(item_list, item_to_remove):
    return list(set(item_list) - {item_to_remove})

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3]
    item_to_remove = 3
    result = remove_duplicates(sample_list, item_to_remove)
    print(result)