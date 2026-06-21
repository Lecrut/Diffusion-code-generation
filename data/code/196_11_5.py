def list_merge(list1, list2):
    return [*list1, *list2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    merged_result = list_merge(sample_list1, sample_list2)
    print(merged_result)