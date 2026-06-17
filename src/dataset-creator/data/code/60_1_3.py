def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        return (year % 100 != 0 or year % 400 == 0)
    else:
        return False
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023, 2028]
    for year in sample_years:
        result = is_leap_year(year)
        print(f"{year}: {'Leap Year' if result else 'Not a Leap Year'}")