def compare_string_sets(set1, set2):
    common_elements = set1.intersection(set2)
    unique_to_set1 = set1.difference(common_elements)
    unique_to_set2 = set2.difference(common_elements)
    return common_elements, unique_to_set1, unique_to_set2

if __name__ == '__main__':
    sample_set1 = {'apple', 'banana', 'cherry', 'date'}
    sample_set2 = {'banana', 'date', 'fig', 'grape'}
    common, unique1, unique2 = compare_string_sets(sample_set1, sample_set2)
    print("Common elements:", common)
    print("Unique to set 1:", unique1)
    print("Unique to set 2:", unique2)