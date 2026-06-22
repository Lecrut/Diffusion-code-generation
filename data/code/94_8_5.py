def verify_truth_presence(data_sequence):
    if not isinstance(data_sequence, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    if len(data_sequence) == 0:
        return False
    
    for item in data_sequence:
        if item is True:
            return True
    
    return False

if __name__ == '__main__':
    test_input = [False, False, True, False]
    outcome = verify_truth_presence(test_input)
    print(outcome)