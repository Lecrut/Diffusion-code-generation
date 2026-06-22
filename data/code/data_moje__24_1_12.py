LEAP_DIVISORS = (4, 100, 400)

def _check_divisibility(year):
    d4 = year % LEAP_DIVISORS[0] == 0
    d100 = year % LEAP_DIVISORS[1] == 0
    d400 = year % LEAP_DIVISORS[2] == 0
    if d400:
        return True
    if d100:
        return False
    if d4:
        return True
    return False

def is_leap_year(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year < 1:
        raise ValueError("Year must be positive")
    return _check_divisibility(year)

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))