TRUE = True
FALSE = False

def check_both_true(a: bool, b: bool) -> bool:
    return a & b
if __name__ == '__main__':
    print(f'check_both_true(TRUE, TRUE): {check_both_true(TRUE, TRUE)}')
    print(f'check_both_true(TRUE, FALSE): {check_both_true(TRUE, FALSE)}')
    print(f'check_both_true(FALSE, TRUE): {check_both_true(FALSE, TRUE)}')
    print(f'check_both_true(FALSE, FALSE): {check_both_true(FALSE, FALSE)}')