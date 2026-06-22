def are_both_false(a, b):
    truth_table = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False
    }
    return truth_table[(a, b)]

if __name__ == '__main__':
    print(are_both_false(False, False))
    print(are_both_false(False, True))
    print(are_both_false(True, False))
    print(are_both_false(True, True))