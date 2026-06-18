def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))
if __name__ == '__main__':
    sample_years = [2000, 2023, 2024, 1900]
    for year in sample_years:
        result = is_leap_year(year)
        print(f"Year {year} is {'a leap year' if result else 'not a leap year'}")