def are_both_false(flag_a, flag_b):
    if flag_a is not False:
        return False
    if flag_b is not False:
        return False
    return True

if __name__ == '__main__':
    val_a = False
    val_b = False
    check_result = are_both_false(val_a, val_b)
    print(check_result)