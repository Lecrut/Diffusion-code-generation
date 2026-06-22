def check_both_false(a, b):
    lookup = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False
    }
    return lookup[(a, b)]

if __name__ == '__main__':
    sample_a = False
    sample_b = False
    result = check_both_false(sample_a, sample_b)
    print(result)
    sample_c = True
    sample_d = False
    result2 = check_both_false(sample_c, sample_d)
    print(result2)