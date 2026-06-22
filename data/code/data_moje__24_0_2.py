def validate_year(year):
    if not isinstance(year, int) or isinstance(year, bool):
        raise TypeError("Year must be an integer")
    if year < 1:
        raise ValueError("Year must be a positive integer")

def is_leap_year(year):
    validate_year(year)
    is_div_400 = (year % 400) == 0
    is_div_100 = (year % 100) == 0
    is_div_4 = (year % 4) == 0
    return is_div_400 or (is_div_4 and not is_div_100)

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(8))
    print(is_leap_year(1))