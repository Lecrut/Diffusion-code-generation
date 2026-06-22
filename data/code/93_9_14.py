def check_both_false(val1, val2):
    truth_table = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False
    }
    return truth_table[(val1, val2)]

if __name__ == '__main__':
    sample1 = check_both_false(False, False)
    sample2 = check_both_false(True, False)
    sample3 = check_both_false(False, True)
    sample4 = check_both_false(True, True)
    print(sample1)
    print(sample2)
    print(sample3)
    print(sample4)