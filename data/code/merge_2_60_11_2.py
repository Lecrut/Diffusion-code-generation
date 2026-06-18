def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False
    if year % 100 == 0:
        return year % 400 == 0
    return True
def validate_input(year) -> bool:
    try:
        int_year = int(year)
        if not isinstance(int_year, int):
            raise TypeError("Input must be an integer.")
        if int_year <= 0:
            raise ValueError(f"Year {int_year} is not a valid input; must be greater than zero.")
        return True
    except (TypeError, ValueError) as e:
        print(f"Input Error: Invalid format or value provided for year '{year}'.")
        return False
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023, -5, "abc", None]
    for year in sample_years:
        if validate_input(year):
            result = is_leap_year(int(year))
            print(f"Year {year} {'is' if result else 'is not'} a leap year.")