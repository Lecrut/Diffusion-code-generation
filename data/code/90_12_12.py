def starts_with_a_or_b(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the list must be strings")
    
    for s in strings:
        if s.startswith('A') or s.startswith('B'):
            return True
    return False

if __name__ == '__main__':
    sample_list1 = ['Apple', 'Banana', 'Cherry']
    sample_list2 = ['Grape', 'Kiwi', 'Lemon']
    
    result1 = starts_with_a_or_b(sample_list1)
    result2 = starts_with_a_or_b(sample_list2)
    
    print(f"Result for sample_list1: {result1}")
    print(f"Result for sample_list2: {result2}")