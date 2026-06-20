def assert_single_true(lst):
    return sum(lst) == 1
if __name__ == '__main__':
    print(assert_single_true([False, True, False]))
    print(assert_single_true([True, False, False]))
    print(assert_single_true([False, False, False]))
    print(assert_single_true([True, True, False]))