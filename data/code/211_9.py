def asymmetric_difference(set1, set2):
    diff1 = set1 - set2
    diff2 = set2 - set1
    return diff1.union(diff2)
if __name__ == '__main__':
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    result = asymmetric_difference(set_a, set_b)
    print(result)