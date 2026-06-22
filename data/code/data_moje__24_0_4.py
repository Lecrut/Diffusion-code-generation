def _is_divisible_by(value, divisor):
    return value % divisor == 0

def _check_positive_integer(year):
    if not isinstance(year, int) or isinstance(year, bool):
        raise TypeError("Year must be an integer")
    if year < 0:
        raise ValueError("Year must be non-negative")

def is_leap_year(year):
    _check_positive_integer(year)
    if _is_divisible_by(year, 400):
        return True
    if _is_divisible_by(year, 100):
        return False
    if _is_divisible_by(year, 4):
        return True
    return False

if __name__ == '__main__':
    print(is_leap_year(2400))
    print(is_leap_year(1800))
    print(is_leap_year(2004))
    print(is_leap_year(2025))