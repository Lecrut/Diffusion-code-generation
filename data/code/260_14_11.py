def compare_sets(set1, set2):
    return max(set1, set2, key=len)

if __name__ == '__main__':
    print(compare_sets({1, 2, 3}, {4, 5}))
    print(compare_sets({}, {1, 2, 3}))
    print(compare_sets({1, 2, 3}, {}))
    print(compare_sets(set(), set()))