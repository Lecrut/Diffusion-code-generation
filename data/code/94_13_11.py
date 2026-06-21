def check_any_match(source, matcher):
    if not hasattr(source, '__iter__'):
        raise ValueError("Source must be iterable")
    
    result = False
    for element in source:
        if matcher(element):
            result = True
            break
    return result

if __name__ == '__main__':
    data = [False, None, 0, [], {}, 42, False]
    condition = lambda val: val is not None and val != 0 and val != [] and val != {}
    outcome = check_any_match(data, condition)
    print(outcome)