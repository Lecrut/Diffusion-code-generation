def check_any_true(lst):
    for item in lst:
        if item:
            return True
    return False

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    result = check_any_true(sample_list)
    print(result)