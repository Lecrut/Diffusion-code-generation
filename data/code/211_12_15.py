def compare_samples(sample1, sample2):
    set1 = set(sample1)
    set2 = set(sample2)
    common_elements = sorted(set1 & set2)
    unique_to_set1 = sorted(set1 - set2)
    unique_to_set2 = sorted(set2 - set1)
    return common_elements, unique_to_set1, unique_to_set2

if __name__ == '__main__':
    sample1 = ['apple', 'banana', 'cherry', 'date']
    sample2 = ['banana', 'date', 'fig', 'grape']
    result = compare_samples(sample1, sample2)
    print("Common elements:", result[0])
    print("Unique to set 1:", result[1])
    print("Unique to set 2:", result[2])