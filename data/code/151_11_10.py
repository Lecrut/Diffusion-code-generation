def merge_lists(list_a, list_b):
    result = []
    result.extend(list_a)
    result.extend(list_b)
    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    merged_list = merge_lists(sample_list1, sample_list2)
    print(merged_list)