def check_any_true(lst):
    found = False
    for item in lst:
        if item:
            found = True
            break
    return found

if __name__ == '__main__':
    sample_list = [False, False, False, True]
    result = check_any_true(sample_list)
    print(result)