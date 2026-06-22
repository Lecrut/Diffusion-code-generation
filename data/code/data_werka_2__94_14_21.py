def contains_true(values):
    if not isinstance(values, (list, tuple, set)):
        raise ValueError("Input must be a list, tuple, or set")
    
    true_set = {True}
    for item in values:
        if item in true_set:
            return True
    return False

if __name__ == '__main__':
    data = [False, False, False, False]
    result = contains_true(data)
    print(result)