def _validate_year(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year <= 0:
        raise ValueError("Year must be a positive integer")

def _is_divisible_by_400(year):
    return year % 400 == 0

def _is_divisible_by_100(year):
    return year % 100 == 0

def _is_divisible_by_4(year):
    return year % 4 == 0

def is_leap_year(year):
    _validate_year(year)
    if _is_divisible_by_400(year):
        return True
    if _is_divisible_by_100(year):
        return False
    return _is_divisible_by_4(year)

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(1234))
    print(is_leap_year(2400))