def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2024) is True
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))