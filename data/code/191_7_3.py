def merge_lists(list_x, list_y):
    return list_x + list_y

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    merged_result = merge_lists(sample_list1, sample_list2)
    print(merged_result)