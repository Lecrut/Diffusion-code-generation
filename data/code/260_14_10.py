def compare_sets(set_a, set_b):
    return max(set_a, set_b, key=len)

if __name__ == '__main__':
    sample_set1 = {3, 5, 2}
    sample_set2 = {4, 6, 1}
    larger_set = compare_sets(sample_set1, sample_set2)
    print(larger_set)