import sys
def is_leap_year(year: int) -> bool:
    if isinstance(year, bool) or not isinstance(year, (int, float)):
        raise TypeError("Input must be an integer representing the year.")
    try:
        year = int(year)
        if year < 0:
            raise ValueError(f"Year {year} cannot exist before the start of our era (Gregorian Calendar starts at year 1).")
    except TypeError:
        raise TypeError("Input must be convertible to an integer.")
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
if __name__ == '__main__':
    sample_years = [2000, 1900, 2023, -5]
    for year in sample_years:
        try:
            result = is_leap_year(year)
            print(f"Year {year}: {'Leap Year' if result else 'Not a Leap Year'}")
        except (TypeError, ValueError) as e:
            print(f"Error processing year {year}: {e}")