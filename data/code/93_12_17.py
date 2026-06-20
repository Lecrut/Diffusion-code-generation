def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    result1 = check_both_false(False, False)
    result2 = check_both_false(False, True)
    print(f"check_both_false(False, False): {result1}")
    print(f"check_both_false(False, True): {result2}")