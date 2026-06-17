def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif (year % 100 != 0) and (year % 4 == 0):
        return True
    elif year % 100 == 0:
        return False
    else:
        return False
if __name__ == '__main__':
    test_years = [1900, 2000, 2024, 2025, 2100]
    print("Leap Year Checker Results:")
    for year in test_years:
        result = is_leap_year(year)
        if result:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is NOT a leap year.")