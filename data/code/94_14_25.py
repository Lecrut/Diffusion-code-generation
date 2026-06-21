def contains_truth(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    true_count = 0
    for item in values:
        if item is True:
            return True
        if item is False:
            continue
        if bool(item):
            return True
            
    return False

if __name__ == '__main__':
    test_cases = [
        [False, False, False],
        [False, True, False],
        [True, True, True],
        [0, 0, 0],
        [1, 0, 0]
    ]
    
    for case in test_cases:
        outcome = contains_truth(case)
        print(outcome)