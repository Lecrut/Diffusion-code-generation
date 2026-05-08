def combine_unique_lists(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    combined_set = set_a.union(set_b)
    return list(combined_set)
if __name__ == '__main__':
    list_a_sample = [1, 2, 3, 4, 4, 5]
    list_b_sample = [4, 5, 6, 7, 8]
    result = combine_unique_lists(list_a_sample, list_b_sample)
    print(result)