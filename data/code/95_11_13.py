def is_all_criteria_met(num):
    return num > 0 and num % 2 == 0 and num < 100

if __name__ == '__main__':
    print(is_all_criteria_met(4))
    print(is_all_criteria_met(3))
    print(is_all_criteria_met(102))
    print(is_all_criteria_met(-2))