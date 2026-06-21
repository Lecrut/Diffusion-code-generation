def merge_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    first_list = [10, 20, 30]
    second_list = ['x', 'y', 'z']
    merged_list = merge_lists(first_list, second_list)
    print(merged_list)