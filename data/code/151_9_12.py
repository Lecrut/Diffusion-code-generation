def merge_lists(list_alpha, list_beta):
    return set().union(*list_alpha, *list_beta)

if __name__ == '__main__':
    sample_list1 = [{1, 2}, {3, 4}]
    sample_list2 = [{4, 5}, {6, 7}]
    result = merge_lists(sample_list1, sample_list2)
    print(result)