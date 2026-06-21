def compare_string_samples(sample1, sample2):
    if not all(isinstance(item, str) for item in sample1 + sample2):
        raise ValueError("Both samples must contain only strings.")
    
    set1 = set(sample1)
    set2 = set(sample2)
    
    common_elements = sorted(set1 & set2)
    unique_to_sample1 = sorted(set1 - set2)
    unique_to_sample2 = sorted(set2 - set1)
    
    return {
        'common': common_elements,
        'unique_to_sample1': unique_to_sample1,
        'unique_to_sample2': unique_to_sample2
    }

if __name__ == '__main__':
    sample1 = ['apple', 'banana', 'cherry', 'date']
    sample2 = ['banana', 'date', 'fig', 'grape']
    
    result = compare_string_samples(sample1, sample2)
    print(result)