def is_leap_year(year: int) -> bool:
    return (year % 400 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0)
if __name__ == '__main__':
    test_years = [2000, 2004, 1900, 2023]
    for year in test_years:
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")