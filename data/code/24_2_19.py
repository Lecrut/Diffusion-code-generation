def _validate_year(year):
    return isinstance(year, int) and year > 0

def is_leap_year(year):
    return _validate_year(year) and (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    years_to_check = [2000, 1900, 2024, 2023, 1600, 2100]
    for y in years_to_check:
        print(is_leap_year(y))