def remove_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    return lst
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(remove_by_index(sample_list, 2))
    print(remove_by_index(sample_list, 0))
    print(remove_by_index(sample_list, -1))
    print(remove_by_index(sample_list, 10))