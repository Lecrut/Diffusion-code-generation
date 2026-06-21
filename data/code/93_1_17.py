def are_both_false(first, second):
    if not isinstance(first, bool) or not isinstance(second, bool):
        raise ValueError("Both arguments must be of type bool")
    
    return first == False and second == False

if __name__ == '__main__':
    test_cases = [
        (False, False),
        (False, True),
        (True, False),
        (True, True)
    ]
    
    for val1, val2 in test_cases:
        output = are_both_false(val1, val2)
        print(output)