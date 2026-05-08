def check_and_combine(a: bool, b: bool) -> bool:
    return a or b
if __name__ == '__main__':
    result1 = check_and_combine(True, False)
    print(f"check_and_combine(True, False): {result1}")
    result2 = check_and_combine(False, True)
    print(f"check_and_combine(False, True): {result2}")
    result3 = check_and_combine(True, True)
    print(f"check_and_combine(True, True): {result3}")
    result4 = check_and_combine(False, False)
    print(f"check_and_combine(False, False): {result4}")