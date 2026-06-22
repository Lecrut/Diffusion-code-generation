FALSE_VALUE = False

def verify_both_false(flag_one, flag_two):
    condition_one = flag_one is FALSE_VALUE
    condition_two = flag_two is FALSE_VALUE
    return condition_one and condition_two

if __name__ == '__main__':
    test_a = False
    test_b = False
    output = verify_both_false(test_a, test_b)
    print(output)