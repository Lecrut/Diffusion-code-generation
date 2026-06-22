def validate_state(flag_a: bool, flag_b: bool, flag_c: bool, flag_d: bool) -> bool:
    if flag_a:
        return flag_b
    if flag_c:
        return not flag_d
    return flag_a or flag_b or flag_c or flag_d

if __name__ == '__main__':
    result = validate_state(True, False, False, True)
    print(result)
    result2 = validate_state(False, False, True, False)
    print(result2)
    result3 = validate_state(False, False, False, False)
    print(result3)