def check_both_true(a: bool, b: bool) -> bool:
    return a and b
if __name__ == '__main__':
    result1 = check_both_true(True, True)
    print(f"check_both_true(True, True): {result1}")
    result2 = check_both_true(True, False)
    print(f"check_both_true(True, False): {result2}")
    result3 = check_both_true(False, True)
    print(f"check_both_true(False, True): {result3}")
    result4 = check_both_true(False, False)
    print(f"check_both_true(False, False): {result4}")