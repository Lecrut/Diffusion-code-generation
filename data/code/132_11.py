def check_logic(a: bool, b: bool) -> bool:
    return a or b
if __name__ == '__main__':
    result1 = check_logic(True, False)
    print(f"check_logic(True, False): {result1}")
    result2 = check_logic(False, True)
    print(f"check_logic(False, True): {result2}")
    result3 = check_logic(True, True)
    print(f"check_logic(True, True): {result3}")
    result4 = check_logic(False, False)
    print(f"check_logic(False, False): {result4}")