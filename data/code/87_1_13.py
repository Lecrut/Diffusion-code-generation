def check_combined_conditions(bool1, bool2):
    if not isinstance(bool1, bool) or not isinstance(bool2, bool):
        raise ValueError("Both arguments must be boolean values.")
    return bool1 or bool2

if __name__ == '__main__':
    result1 = check_combined_conditions(True, False)
    print(result1)
    result2 = check_combined_conditions(False, True)
    print(result2)
    result3 = check_combined_conditions(True, True)
    print(result3)
    result4 = check_combined_conditions(False, False)
    print(result4)