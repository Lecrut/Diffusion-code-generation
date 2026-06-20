def contains_true(lst):
    for element in lst:
        if element:
            return True
    return False

if __name__ == '__main__':
    sample_list = [False, False, False, True]
    result = contains_true(sample_list)
    print(result)