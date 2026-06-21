def compare_sets(set1, set2):
    unique_to_set1 = set1 - set2
    unique_to_set2 = set2 - set1
    common_elements = set1 & set2
    return (unique_to_set1, unique_to_set2, common_elements)

if __name__ == '__main__':
    sample_set1 = {10, 20, 30, 40}
    sample_set2 = {30, 40, 50, 60}
    result = compare_sets(sample_set1, sample_set2)
    print(result)