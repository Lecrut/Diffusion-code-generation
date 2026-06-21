def compare_samples(sample1, sample2):
    set1 = set(sample1)
    set2 = set(sample2)
    
    common_elements = set1.intersection(set2)
    unique_to_sample1 = set1.difference(common_elements)
    unique_to_sample2 = set2.difference(common_elements)
    
    return common_elements, unique_to_sample1, unique_to_sample2

if __name__ == '__main__':
    sample1 = ['apple', 'banana', 'cherry', 'date']
    sample2 = ['banana', 'grape', 'orange', 'date']
    
    common, unique1, unique2 = compare_samples(sample1, sample2)
    
    print("Common elements:", common)
    print("Unique to sample 1:", unique1)
    print("Unique to sample 2:", unique2)