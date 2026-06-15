def merge_lists(list1, list2):
    merged_list = list(list1)
    merged_list.extend(list2)
    return merged_list
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result = merge_lists(list_a, list_b)
    print(result)