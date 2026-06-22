def contains_a_or_b_prefix(strings):
    if not isinstance(strings, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    def validate_string(item):
        if not isinstance(item, str):
            raise ValueError("All items must be strings")
        return item
    
    def check_prefix(item):
        validated = validate_string(item)
        if not validated:
            return False
        first_char = validated[0]
        return first_char == 'A' or first_char == 'B'
    
    for item in strings:
        if check_prefix(item):
            return True
    return False

if __name__ == '__main__':
    test_strings = ['Apple', 'Banana', 'Cherry']
    output = contains_a_or_b_prefix(test_strings)
    print(output)