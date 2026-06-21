def remove_item_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    return lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    index_to_remove = 2
    updated_list = remove_item_by_index(sample_list, index_to_remove)
    print(updated_list)