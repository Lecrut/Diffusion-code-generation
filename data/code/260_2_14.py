def find_common_elements(set1, set2):
    return set1 & set2

if __name__ == '__main__':
    sample_set_a = {1, 2, 3, 4, 5}
    sample_set_b = {4, 5, 6, 7, 8}
    print(find_common_elements(sample_set_a, sample_set_b))