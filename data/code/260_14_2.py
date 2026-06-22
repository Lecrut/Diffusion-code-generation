def compare_sets(set_a, set_b):
    return max(set_a, set_b)

if __name__ == '__main__':
    sample_set_1 = {3, 5, 2}
    sample_set_2 = {4, 6, 1}
    print(compare_sets(sample_set_1, sample_set_2))