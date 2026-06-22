def check_both_false(x, y):
    truth_table = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False
    }
    return truth_table[(x, y)]

if __name__ == '__main__':
    val1 = False
    val2 = False
    result = check_both_false(val1, val2)
    print(result)
    result2 = check_both_false(True, False)
    print(result2)