def is_subset(subset, master):
    if not isinstance(subset, list) or not isinstance(master, list):
        raise ValueError('Both arguments must be lists.')
    subset_set = set(subset)
    master_set = set(master)
    return subset_set.issubset(master_set)
if __name__ == '__main__':
    group_a = [101, 102, 103, 104, 105]
    group_b = [104, 105, 106, 107, 108]
    result = is_subset(group_a, group_b)
    print(result)