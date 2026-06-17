def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 != 0:
            return True
    return False
if __name__ == '__main__':
    sample_years = [2000, 1900, 2004, 2003, 2024]
    print("Leap Year Analysis Results:")
    for year in sample_years:
        result = is_leap_year(year)
        if result:
            print(f"{year} is a LEAP YEAR.")
        else:
            print(f"{year} is NOT a leap year (common year).")