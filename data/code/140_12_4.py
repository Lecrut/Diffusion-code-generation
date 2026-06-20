def validate_input(value):
    if isinstance(value, str) and value:
        return bool(re.match('^[a-zA-Z0-9]+$', value))
    elif isinstance(value, int) and value > 0:
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        ('Hello123', True),
        (42, True),
        ('', False),
        ('Hello!', False),
        (-5, False)
    ]
    
    for i, (input_val, expected) in enumerate(test_cases):
        result = validate_input(input_val)
        print(f"Test Case {i+1}: Input({input_val}) -> Expected: {expected}, Got: {result}")