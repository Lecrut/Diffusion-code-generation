def find_common_and_unique(sample1, sample2):
    set1 = set(sample1)
    set2 = set(sample2)
    common_elements = sorted(set1 & set2)
    unique_to_set1 = sorted(set1 - set2)
    unique_to_set2 = sorted(set2 - set1)
    return common_elements, unique_to_set1, unique_to_set2

if __name__ == '__main__':
    sample1 = ['apple', 'banana', 'cherry', 'date']
    sample2 = ['banana', 'dragonfruit', 'elderberry', 'fig']
    result_common, result_unique1, result_unique2 = find_common_and_unique(sample1, sample2)
    print("Common Elements:", result_common)
    print("Unique to Set 1:", result_unique1)
    print("Unique to Set 2:", result_unique2)