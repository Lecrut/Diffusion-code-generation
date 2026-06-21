def merge_lists(list_x, list_y):
    return list_x + list_y

if __name__ == '__main__':
    LIST_X = [1, 2, 3]
    LIST_Y = ['a', 'b', 'c']
    merged_list = merge_lists(LIST_X, LIST_Y)
    print(merged_list)