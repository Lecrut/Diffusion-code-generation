def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    return year % 400 == 0

if __name__ == '__main__':
    print(is_leap_year(1996))
    print(is_leap_year(2100))
    print(is_leap_year(2000))
    print(is_leap_year(2023))