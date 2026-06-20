def check_user_access(is_active: bool, has_permission: bool) -> bool:
    access_mapping = {
        (True, True): True,
        (False, False): False,
        (True, False): False,
        (False, True): False
    }
    return access_mapping[(is_active, has_permission)]

if __name__ == '__main__':
    check1 = True
    check2 = False
    result1 = check_user_access(check1, check2)
    print(f"Access with {check1} active and {check2} permission: {result1}")
    check3 = True
    check4 = True
    result2 = check_user_access(check3, check4)
    print(f"Access with {check3} active and {check4} permission: {result2}")
    check5 = False
    check6 = False
    result3 = check_user_access(check5, check6)
    print(f"Access with {check5} active and {check6} permission: {result3}")