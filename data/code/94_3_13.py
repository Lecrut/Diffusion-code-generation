def contains_true(lst):
    if not isinstance(lst, list) or not all(isinstance(x, bool) for x in lst):
        raise ValueError("Input must be a list of booleans")
    return any(lst)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    print(contains_true(sample_list))