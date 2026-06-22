def compare_sets(set1, set2):
    return [x for x in set1 if x > max(set2)] + [y for y in set2 if y > max(set1)]

if __name__ == '__main__':
    sample_set1 = {5, 6, 7, 8}
    sample_set2 = {3, 4, 9, 10}
    print(compare_sets(sample_set1, sample_set2))