def can_proceed(is_active: bool, has_permission: bool) -> bool:
    return is_active and has_permission

if __name__ == '__main__':
    check1 = True
    check2 = False
    result1 = can_proceed(check1, check2)
    print(f"Proceed with {check1} active and {check2} permission: {result1}")
    
    check3 = True
    check4 = True
    result2 = can_proceed(check3, check4)
    print(f"Proceed with {check3} active and {check4} permission: {result2}")
    
    check5 = False
    check6 = False
    result3 = can_proceed(check5, check6)
    print(f"Proceed with {check5} active and {check6} permission: {result3}")