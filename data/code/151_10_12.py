def merge_lists(list1, list2):
    result = []
    for item in list1:
        if item not in result:
            result.append(item)
    for item in list2:
        if item not in result:
            result.append(item)
    return result
if __name__ == '__main__':
    sample_list_a = [1, 2, 3, 4]
    sample_list_b = [3, 4, 5, 6]
    merged_result = merge_lists(sample_list_a, sample_list_b)
    print(merged_result)