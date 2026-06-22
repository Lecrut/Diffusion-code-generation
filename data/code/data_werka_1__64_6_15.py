def find_last_index(lst, item):
    last_index = -1
    for index in range(len(lst)):
        if lst[index] == item:
            last_index = index
    return last_index
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    item_to_find = 3
    print(find_last_index(sample_list, item_to_find))
    empty_list = []
    print(find_last_index(empty_list, item_to_find))
    no_match_list = [1, 2, 4, 5]
    print(find_last_index(no_match_list, item_to_find))