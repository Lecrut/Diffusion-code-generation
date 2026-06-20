def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    print(f"Test 1 (False, False): {check_both_false(False, False)}")
    print(f"Test 2 (True, False): {check_both_false(True, False)}")
    print(f"Test 3 (True, True): {check_both_false(True, True)}")
    print(f"Test 4 (False, True): {check_both_false(False, True)}")