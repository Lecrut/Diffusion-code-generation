def remove_item_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    index_to_remove = 2
    remove_item_by_index(sample_list, index_to_remove)
    print(sample_list)