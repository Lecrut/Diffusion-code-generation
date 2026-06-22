def check_prefix_a_or_b(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    
    target_chars = frozenset(['A', 'B'])
    
    for element in input_list:
        if not isinstance(element, str):
            raise ValueError("All elements must be strings")
        if len(element) > 0 and element[0] in target_chars:
            return True
    return False

if __name__ == '__main__':
    test_data = ['Zebra', 'Bat', 'Ant']
    outcome = check_prefix_a_or_b(test_data)
    print(outcome)