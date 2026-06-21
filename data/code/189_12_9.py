def remove_item_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original list:", sample_list)
    remove_item_by_index(sample_list, 2)
    print("List after removing item at index 2:", sample_list)