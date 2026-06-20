def check_combined_conditions(cond1, cond2):
    return cond1 or cond2

if __name__ == '__main__':
    print(check_combined_conditions(True, False))
    print(check_combined_conditions(False, True))
    print(check_combined_conditions(True, True))
    print(check_combined_conditions(False, False))