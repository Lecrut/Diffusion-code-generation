def check_conditions(condition_a: bool, condition_b: bool) -> bool:
    return condition_a and condition_b
if __name__ == '__main__':
    result1 = check_conditions(True, True)
    print(f"check_conditions(True, True): {result1}")
    result2 = check_conditions(True, False)
    print(f"check_conditions(True, False): {result2}")
    result3 = check_conditions(False, True)
    print(f"check_conditions(False, True): {result3}")
    result4 = check_conditions(False, False)
    print(f"check_conditions(False, False): {result4}")