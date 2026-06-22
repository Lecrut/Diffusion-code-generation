def find_unique_elements(primary_list, comparison_list):
    primary_set = set(primary_list)
    comparison_set = set(comparison_list)
    unique_elements = primary_set.difference(comparison_set)
    return list(unique_elements)

if __name__ == '__main__':
    sample_primary_list = [100, 200, 300, 400, 500]
    sample_comparison_list = [300, 400, 600, 700, 800]
    result = find_unique_elements(sample_primary_list, sample_comparison_list)
    print(result)