def find_common_and_unique(sample1, sample2):
    set1 = set(sample1)
    set2 = set(sample2)
    common_elements = set1 & set2
    unique_to_set1 = set1 - set2
    unique_to_set2 = set2 - set1
    return sorted(common_elements), sorted(unique_to_set1), sorted(unique_to_set2)

if __name__ == '__main__':
    sample1 = ["apple", "banana", "cherry", "date"]
    sample2 = ["banana", "date", "fig", "grape"]
    common, unique_to_first, unique_to_second = find_common_and_unique(sample1, sample2)
    print("Common elements:", common)
    print("Unique to first set:", unique_to_first)
    print("Unique to second set:", unique_to_second)