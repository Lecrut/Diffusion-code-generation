def _is_positive_integer(value):
    return isinstance(value, int) and not isinstance(value, bool) and value > 0

def _validate_year(year):
    if not _is_positive_integer(year):
        raise ValueError("Year must be a positive integer")
    return year

def is_leap_year(year):
    _validate_year(year)
    remainder_400 = year % 400
    remainder_100 = year % 100
    remainder_4 = year % 4
    if remainder_400 == 0:
        return True
    if remainder_100 == 0:
        return False
    if remainder_4 == 0:
        return True
    return False

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))