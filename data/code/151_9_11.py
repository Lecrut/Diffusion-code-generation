def merge_sets(list1, list2):
    combined_set = set()
    for sublist in list1:
        combined_set.update(sublist)
    for sublist in list2:
        combined_set.update(sublist)
    return combined_set

if __name__ == '__main__':
    sample_list1 = [{1, 3}, {5, 7}]
    sample_list2 = [{3, 5}, {9, 11}]
    result = merge_sets(sample_list1, sample_list2)
    print(result)