def contains_true(lst):
    return any(lst)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = contains_true(sample_list)
    print(result)