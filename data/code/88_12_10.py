def check_both_true(a: bool, b: bool) -> bool:
    return a & b

if __name__ == '__main__':
    result1 = check_both_true(True, True)
    result2 = check_both_true(False, False)
    result3 = check_both_true(True, False)
    result4 = check_both_true(False, True)
    
    print(f"check_both_true(True, True): {result1}")
    print(f"check_both_true(False, False): {result2}")
    print(f"check_both_true(True, False): {result3}")
    print(f"check_both_true(False, True): {result4}")