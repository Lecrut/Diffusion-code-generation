def is_subset(list_a, list_b):
    return set(list_a).issubset(set(list_b))

if __name__ == '__main__':
    group_a = [101, 102, 103, 104, 105]
    group_b = [104, 105, 106, 107, 108]
    print(is_subset(group_a, group_b))