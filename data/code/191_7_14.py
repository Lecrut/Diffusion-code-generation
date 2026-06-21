def merge_lists(list_a, list_b):
    return list_a + list_b

if __name__ == '__main__':
    first_list = [10, 20, 30]
    second_list = ['x', 'y', 'z']
    merged_lists = merge_lists(first_list, second_list)
    print(merged_lists)