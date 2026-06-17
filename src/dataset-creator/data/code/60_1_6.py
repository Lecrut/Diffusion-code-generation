def is_leap_year(year: int) -> bool:
    if not isinstance(year, int):
        raise TypeError(f"Expected an integer for year, got {type(year).__name__}")
    if year < -2798 or year > 9999:
        raise ValueError(f"Year must be between -2798 and 9999, got {year}.")
    return (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))
if __name__ == '__main__':
    sample_years = [2000, 1900, 2023, 2024, -800]
    for year in sample_years:
        result = is_leap_year(year)
        print(f"{year} is {'a' if result else 'not'} a leap year.")