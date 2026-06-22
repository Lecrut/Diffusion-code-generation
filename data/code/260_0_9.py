def compare_sets(set1, set2):
    larger_set = [x for x in set1 if x > max(set2)] + [y for y in set2 if y > max(set1)]
    return larger_set

if __name__ == '__main__':
    sample_set1 = {10, 20, 30}
    sample_set2 = {5, 15, 25, 40}
    result = compare_sets(sample_set1, sample_set2)
    print(result)