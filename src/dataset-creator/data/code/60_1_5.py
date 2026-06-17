def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    sample_years = [2000, 2004, 2005, 2100]
    for year in sample_years:
        result = is_leap_year(year)
        print(f"{year} is {'a leap year' if result else 'not a leap year'}")