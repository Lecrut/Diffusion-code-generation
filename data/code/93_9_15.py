def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    result1 = check_both_false(False, False)
    print(f"Test 1 (False, False): {result1}")
    result2 = check_both_false(True, True)
    print(f"Test 2 (True, True): {result2}")
    result3 = check_both_false(False, True)
    print(f"Test 3 (False, True): {result3}")