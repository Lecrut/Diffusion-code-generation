def any_true(boolean_list):
    return any(boolean_list)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = any_true(sample_list)
    print(result)