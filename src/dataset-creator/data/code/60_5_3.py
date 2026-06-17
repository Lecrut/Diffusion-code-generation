def calculate_leap_year_status(year):
    if year % 400 == 0:
        return True
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        return False
    pass
def calculate_leap_year_status_v2(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
def main():
    test_year_1 = 2000
    result_1 = calculate_leap_year_status_v2(test_year_1)
    print(f"Year {test_year_1}: {'Leap Year' if result_1 else 'Not a Leap Year'}")
    test_year_2 = 1900
    result_2 = calculate_leap_year_status_v2(test_year_2)
    print(f"Year {test_year_2}: {'Leap Year' if result_2 else 'Not a Leap Year'}")
    test_year_3 = 2024
    result_3 = calculate_leap_year_status_v2(test_year_3)
    print(f"Year {test_year_3}: {'Leap Year' if result_3 else 'Not a Leap Year'}")
    test_year_4 = 2023
    result_4 = calculate_leap_year_status_v2(test_year_4)
    print(f"Year {test_year_4}: {'Leap Year' if result_4 else 'Not a Leap Year'}")
if __name__ == '__main__':
    main()