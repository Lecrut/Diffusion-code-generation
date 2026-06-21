def remove_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original list:", sample_list)
    remove_by_index(sample_list, 2)
    print("Modified list:", sample_list)