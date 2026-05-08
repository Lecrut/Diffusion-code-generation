def combine_lists_optimized(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    union_set = set_a.union(set_b)
    return list(union_set)
if __name__ == '__main__':
    list_a_sample = [1, 2, 3, 4, 5, 2]
    list_b_sample = [4, 5, 6, 7, 8, 1]
    result = combine_lists_optimized(list_a_sample, list_b_sample)
    print(result)