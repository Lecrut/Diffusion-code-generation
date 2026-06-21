def any_element_meets_criteria(iterable, criterion):
    MATCH_THRESHOLD = 1
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    found_match = False
    for element in iterable:
        if criterion(element):
            found_match = True
            break
            
    return found_match

if __name__ == '__main__':
    data_values = [0, 0, 0, 0, 5, 0]
    check_positive = lambda val: val > 0
    output = any_element_meets_criteria(data_values, check_positive)
    print(output)