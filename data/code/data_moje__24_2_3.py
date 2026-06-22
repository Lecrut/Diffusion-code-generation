def check_leap_status(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    test_years = [2100, 2000, 2024, 2023, 1600, 1999]
    for current_year in test_years:
        result = check_leap_status(current_year)
        print(f"Year {current_year}: {result}")