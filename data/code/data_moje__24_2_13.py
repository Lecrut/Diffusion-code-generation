def _validate_year(y):
    return isinstance(y, int) and y > 0

def is_leap_year(year):
    return _validate_year(year) and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(2100))
    print(is_leap_year(1600))