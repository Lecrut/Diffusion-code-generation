def contains_true(lst):
    return any(lst)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    print(contains_true(sample_list))