def check_or_condition(a: bool, b: bool) -> bool:
    return a or b
if __name__ == '__main__':
    result1 = check_or_condition(True, False)
    print(f"check_or_condition(True, False): {result1}")
    result2 = check_or_condition(False, True)
    print(f"check_or_condition(False, True): {result2}")
    result3 = check_or_condition(True, True)
    print(f"check_or_condition(True, True): {result3}")
    result4 = check_or_condition(False, False)
    print(f"check_or_condition(False, False): {result4}")