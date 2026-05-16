def check_both(a: bool, b: bool) -> bool:
    return a and b
if __name__ == '__main__':
    result1 = check_both(True, True)
    print(f"check_both(True, True): {result1}")
    result2 = check_both(True, False)
    print(f"check_both(True, False): {result2}")
    result3 = check_both(False, True)
    print(f"check_both(False, True): {result3}")
    result4 = check_both(False, False)
    print(f"check_both(False, False): {result4}")