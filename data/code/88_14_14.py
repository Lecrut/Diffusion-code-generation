TRUE = True
FALSE = False

def is_both_true(value1, value2):
    return value1 and value2
if __name__ == '__main__':
    print(is_both_true(TRUE, TRUE))
    print(is_both_true(TRUE, FALSE))
    print(is_both_true(FALSE, TRUE))
    print(is_both_true(FALSE, FALSE))