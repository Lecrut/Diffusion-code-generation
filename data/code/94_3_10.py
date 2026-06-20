def contains_true(lst):
    if not all(isinstance(item, bool) for item in lst):
        raise ValueError("List must contain only boolean values")
    return any(lst)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = contains_true(sample_list)
    print(result)