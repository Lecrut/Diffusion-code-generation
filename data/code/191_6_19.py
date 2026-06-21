def merge_lists(list1, list2):
    merged_list = list1.copy()
    merged_list.extend(list2)
    return merged_list
if __name__ == '__main__':
    sample_list1 = ['red', 'green']
    sample_list2 = ['blue', 'yellow']
    result = merge_lists(sample_list1, sample_list2)
    print(result)