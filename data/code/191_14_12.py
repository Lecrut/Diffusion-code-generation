def merge_lists(list1, list2):
    return [item for sublist in (list1, list2) for item in sublist]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = ['x', 'y', 'z']
    merged_result = merge_lists(sample_list1, sample_list2)
    print(merged_result)