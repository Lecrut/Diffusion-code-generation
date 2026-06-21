def is_leap_year(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year < 1:
        raise ValueError("Year must be positive")
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0
    if not divisible_by_4:
        return False
    if divisible_by_100 and not divisible_by_400:
        return False
    return True

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(1600))
    print(is_leap_year(1700))