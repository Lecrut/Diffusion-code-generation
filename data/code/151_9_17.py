def merge_sets(list1, list2):
    SET_UNION = set().union
    return SET_UNION(*list1, *list2)

if __name__ == '__main__':
    sample_list1 = [{1, 2}, {3, 4}]
    sample_list2 = [{4, 5}, {6, 7}]
    result = merge_sets(sample_list1, sample_list2)
    print(result)