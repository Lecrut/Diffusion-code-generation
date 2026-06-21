def merge_lists_of_sets(list_alpha, list_beta):
    if not all(isinstance(lst, list) for lst in (list_alpha, list_beta)):
        raise ValueError("Both inputs must be lists")
    if not all(all(isinstance(s, set) for s in sublist) for sublist in (list_alpha, list_beta)):
        raise ValueError("All elements in the lists must be sets")

    combined_set = set().union(*list_alpha, *list_beta)
    return combined_set

if __name__ == '__main__':
    sample_list1 = [{1, 2}, {3, 4}]
    sample_list2 = [{4, 5}, {6, 7}]
    result = merge_lists_of_sets(sample_list1, sample_list2)
    print(result)