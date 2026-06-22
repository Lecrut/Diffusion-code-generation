def any_true(values):
    return any(values)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = any_true(sample_list)
    print(result)