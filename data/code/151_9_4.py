def merge_sets(list1, list2):
    combined_set = set()
    for item in list1:
        combined_set.update(item)
    for item in list2:
        combined_set.update(item)
    return combined_set

if __name__ == '__main__':
    sample_list1 = [{1, 3}, {5, 7}]
    sample_list2 = [{4, 6}, {8, 10}]
    result = merge_sets(sample_list1, sample_list2)
    print(result)