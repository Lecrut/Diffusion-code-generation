def check_or_condition(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean values")
    return a or b

if __name__ == '__main__':
    try:
        result1 = check_or_condition(True, False)
        print(f"check_or_condition(True, False): {result1}")
        
        result2 = check_or_condition(False, True)
        print(f"check_or_condition(False, True): {result2}")
        
        result3 = check_or_condition(True, True)
        print(f"check_or_condition(True, True): {result3}")
        
        result4 = check_or_condition(False, False)
        print(f"check_or_condition(False, False): {result4}")
    except ValueError as e:
        print(e)