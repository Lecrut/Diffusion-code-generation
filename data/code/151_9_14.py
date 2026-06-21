def merge_set_lists(list_alpha, list_beta):
    set_union = set().union(*list_alpha, *list_beta)
    return set_union

if __name__ == '__main__':
    sample_list1 = [{1, 2}, {3, 4}]
    sample_list2 = [{4, 5}, {6, 7}]
    result = merge_set_lists(sample_list1, sample_list2)
    print(result)