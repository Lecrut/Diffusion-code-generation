FALSE = False

def are_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    print(are_both_false(FALSE, FALSE))
    print(are_both_false(FALSE, TRUE))
    print(are_both_false(TRUE, FALSE))
    print(are_both_false(TRUE, TRUE))