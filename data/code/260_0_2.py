def compare_sets(set1, set2):
    return [x for x in set1 if x > max(set2)] + [y for y in set2 if y > max(set1)]

if __name__ == '__main__':
    sample_set1 = {5, 3, 9, 7}
    sample_set2 = {4, 6, 8, 10}
    print(compare_sets(sample_set1, sample_set2))