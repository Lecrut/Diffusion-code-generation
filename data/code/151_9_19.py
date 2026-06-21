def merge_sets(list_alpha, list_beta):
    combined_set = set().union(*list_alpha, *list_beta)
    return combined_set

if __name__ == '__main__':
    sample_list1 = [{1, 2}, {3, 4}]
    sample_list2 = [{4, 5}, {6, 7}]
    result = merge_sets(sample_list1, sample_list2)
    print(result)