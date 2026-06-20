def check_at_least_one_true(bool_list):
    if not isinstance(bool_list, list) or not all(isinstance(item, bool) for item in bool_list):
        raise ValueError("Input must be a list of boolean values")
    
    return any(bool_list)

if __name__ == '__main__':
    sample_list = [False, False, True, False, False]
    result = check_at_least_one_true(sample_list)
    print(result)