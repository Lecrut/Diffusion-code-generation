def any_true(values):
    for val in values:
        if val:
            return True
    return False

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = any_true(sample_list)
    print(result)