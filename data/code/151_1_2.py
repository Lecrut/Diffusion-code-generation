def union_optimized(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    union_set = set_a.union(set_b)
    return list(union_set)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5]
    list_b = [4, 5, 6, 7, 8, 8]
    result = union_optimized(list_a, list_b)
    print(result)