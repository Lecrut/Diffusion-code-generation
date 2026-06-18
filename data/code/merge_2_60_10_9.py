def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    sample_years = [2000, 2001, 2004, 2100]
    for test_year in sample_years:
        result = is_leap_year(test_year)
        print(f"{test_year} is a leap year" if result else f"{test_year} is not a leap year")