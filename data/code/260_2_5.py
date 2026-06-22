def find_common_elements(set1, set2):
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    common_elements = find_common_elements(sample_set1, sample_set2)
    print(common_elements)