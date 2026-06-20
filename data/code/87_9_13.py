def can_proceed(is_active: bool, has_permission: bool) -> bool:
    return is_active and has_permission

if __name__ == '__main__':
    check1 = True
    check2 = False
    result1 = can_proceed(check1, check2)
    print(f"Proceed with checks {check1} and {check2}: {result1}")
    
    check3 = True
    check4 = True
    result2 = can_proceed(check3, check4)
    print(f"Proceed with checks {check3} and {check4}: {result2}")