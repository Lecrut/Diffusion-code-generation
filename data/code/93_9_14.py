BOOLEAN_FALSE = False

def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    result1 = check_both_false(BOOLEAN_FALSE, BOOLEAN_FALSE)
    print(f"Test 1 (False, False): {result1}")
    result2 = check_both_false(True, BOOLEAN_FALSE)
    print(f"Test 2 (True, False): {result2}")
    result3 = check_both_false(True, True)
    print(f"Test 3 (True, True): {result3}")
    result4 = check_both_false(BOOLEAN_FALSE, True)
    print(f"Test 4 (False, True): {result4}")