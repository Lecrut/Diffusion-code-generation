def larger_set(set_a, set_b):
    return max(set_a, set_b)

if __name__ == '__main__':
    sample_set1 = {3, 5, 2}
    sample_set2 = {4, 6, 1}
    print(larger_set(sample_set1, sample_set2))