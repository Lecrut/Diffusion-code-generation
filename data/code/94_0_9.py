def check_at_least_one_true(bool_list):
    if not all(isinstance(item, bool) for item in bool_list):
        raise ValueError("All elements in the list must be boolean values.")
    
    return any(bool_list)

if __name__ == '__main__':
    sample_list = [False, False, True, False, False]
    result = check_at_least_one_true(sample_list)
    print(result)