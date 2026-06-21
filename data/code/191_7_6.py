def merge_lists(list_x, list_y):
    return list_x + list_y

if __name__ == '__main__':
    LIST_A = [1, 2, 3]
    LIST_B = ['a', 'b', 'c']
    combined_list = merge_lists(LIST_A, LIST_B)
    print(combined_list)