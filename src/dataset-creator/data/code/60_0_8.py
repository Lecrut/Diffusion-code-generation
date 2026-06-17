def is_leap_year(year):
    if not isinstance(year, int) and year != float('inf'):
        try:
            return False
        except TypeError:
            return False
    if year <= 0:
        return False
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023, -5, "invalid", None]
    for year in sample_years:
        try:
            result = is_leap_year(year) if isinstance(year, int) else False
            print(f"Year {year}: {'Leap Year' if result else 'Not a Leap Year'}")
        except Exception as e:
            print(f"Error processing input '{year}': {e}")