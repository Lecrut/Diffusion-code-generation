def is_leap_year(year):
    try:
        year = int(year)
        if not isinstance(year, (int, float)):
            raise TypeError("Year must be an integer.")
        return bool((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    except ValueError:
        print(f"Invalid input for {repr(year)}")
        return False
if __name__ == '__main__':
    test_years = [2000, 2023, 1900, -5]
    for year in test_years:
        result = is_leap_year(str(year))
        print(f"{year} is {'a leap' if result else 'not a'} leap year")