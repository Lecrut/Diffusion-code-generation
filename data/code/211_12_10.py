def find_common_and_unique(sample1, sample2):
    set1 = set(sample1)
    set2 = set(sample2)
    
    common_elements = set1.intersection(set2)
    unique_elements_sample1 = set1 - common_elements
    unique_elements_sample2 = set2 - common_elements
    
    return common_elements, unique_elements_sample1, unique_elements_sample2

def validate_inputs(sample1, sample2):
    if not all(isinstance(item, str) for item in sample1 + sample2):
        raise ValueError("Both samples must contain only strings.")
    
if __name__ == '__main__':
    sample1 = ["apple", "banana", "cherry", "date"]
    sample2 = ["banana", "date", "fig", "grape"]
    
    validate_inputs(sample1, sample2)
    common, unique1, unique2 = find_common_and_unique(sample1, sample2)
    print("Common elements:", sorted(common))
    print("Unique to sample1:", sorted(unique1))
    print("Unique to sample2:", sorted(unique2))