def _validate_year(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year <= 0:
        raise ValueError("Year must be a positive integer")

def is_leap_year(year):
    _validate_year(year)
    is_divisible_by_four = year % 4 == 0
    is_divisible_by_hundred = year % 100 == 0
    is_divisible_by_four_hundred = year % 400 == 0
    if is_divisible_by_four_hundred:
        return True
    if is_divisible_by_hundred:
        return False
    return is_divisible_by_four

if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023, 2100, 2400]
    for y in sample_years:
        print(y, is_leap_year(y))
    try:
        is_leap_year("2000")
    except TypeError as e:
        print(e)
    try:
        is_leap_year(-10)
    except ValueError as e:
        print(e)