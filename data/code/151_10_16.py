def concatenate_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    list_x = [10, 20, 30]
    list_y = [40, 50, 60]
    combined_list = concatenate_lists(list_x, list_y)
    print(combined_list)