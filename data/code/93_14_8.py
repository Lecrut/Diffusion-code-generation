FALSE = False

def check_both_false(a: bool, b: bool) -> bool:
    return not (a | b)

if __name__ == '__main__':
    print(check_both_false(FALSE, FALSE))
    print(check_both_false(TRUE, FALSE))
    print(check_both_false(FALSE, TRUE))
    print(check_both_false(TRUE, TRUE))