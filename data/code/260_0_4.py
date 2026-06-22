def compare_sets(set1, set2):
    return [x for x in set1 if x > max(set2)] + [y for y in set2 if y > max(set1)]

if __name__ == '__main__':
    sample_set1 = {3, 5, 7, 9}
    sample_set2 = {2, 4, 6, 8}
    print(compare_sets(sample_set1, sample_set2))