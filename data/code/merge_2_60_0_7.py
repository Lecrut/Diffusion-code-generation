def is_leap_year(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023, "invalid", -5]
    for year in sample_years:
        try:
            result = is_leap_year(year)
            print(f"{year} is a leap year" if result else f"{year} is not a leap year")
        except TypeError as e:
            print(f"Error processing {type(year).__name__}: {e}")