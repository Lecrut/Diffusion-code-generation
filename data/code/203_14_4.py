def compare_sets(set1, set2):
    unique_to_set1 = set1 - set2
    unique_to_set2 = set2 - set1
    common_elements = set1 & set2
    return (unique_to_set1, unique_to_set2, common_elements)

if __name__ == '__main__':
    sample_set_a = {7, 8, 9}
    sample_set_b = {9, 10, 11}
    result = compare_sets(sample_set_a, sample_set_b)
    print(result)