def compare_string_samples(sample1, sample2):
    set1 = set(sample1)
    set2 = set(sample2)
    
    common_elements = set1.intersection(set2)
    unique_to_set1 = set1 - set2
    unique_to_set2 = set2 - set1
    
    return {
        "common": sorted(list(common_elements)),
        "unique_to_set1": sorted(list(unique_to_set1)),
        "unique_to_set2": sorted(list(unique_to_set2))
    }

if __name__ == '__main__':
    sample1 = ["apple", "banana", "cherry"]
    sample2 = ["banana", "date", "fig"]
    result = compare_string_samples(sample1, sample2)
    print(result)