def any_true(lst):
    if not all(isinstance(x, bool) for x in lst):
        raise ValueError("List must contain only boolean values")
    return any(lst)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    print(any_true(sample_list))