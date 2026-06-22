def compare_sets(set_a, set_b):
    return max(set_a, set_b, key=len)

if __name__ == '__main__':
    sample_set1 = {10, 20, 30, 40}
    sample_set2 = {5, 15, 25, 35, 45, 50}
    larger_set = compare_sets(sample_set1, sample_set2)
    print(larger_set)