def any_true(bool_list):
    return any(bool_list)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = any_true(sample_list)
    print(result)