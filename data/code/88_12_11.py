TRUE = 1
FALSE = 0

def check_both_true(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    print(f"check_both_true(True, True): {check_both_true(TRUE, TRUE)}")
    print(f"check_both_true(True, False): {check_both_true(TRUE, FALSE)}")
    print(f"check_both_true(False, True): {check_both_true(FALSE, TRUE)}")
    print(f"check_both_true(False, False): {check_both_true(FALSE, FALSE)}")