def compare_sets(set1, set2):
    unique_set1 = set1 - set2
    unique_set2 = set2 - set1
    common_elements = set1 & set2
    return (unique_set1, unique_set2, common_elements)
if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    result = compare_sets(sample_set1, sample_set2)
    print(result)