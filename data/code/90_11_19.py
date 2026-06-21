def contains_a_or_b_prefix(strings):
    if not isinstance(strings, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    valid_prefixes = ('A', 'B')
    
    for item in strings:
        if not isinstance(item, str):
            raise ValueError("All items must be strings")
        if item and item[0] in valid_prefixes:
            return True
    return False

if __name__ == '__main__':
    test_list = ['Dog', 'Apple', 'Cat']
    outcome = contains_a_or_b_prefix(test_list)
    print(outcome)