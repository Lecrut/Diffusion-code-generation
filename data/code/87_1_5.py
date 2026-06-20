def check_combined_conditions(a, b):
    return a or b

if __name__ == '__main__':
    print(check_combined_conditions(True, False))
    print(check_combined_conditions(False, True))
    print(check_combined_conditions(False, False))
    print(check_combined_conditions(True, True))