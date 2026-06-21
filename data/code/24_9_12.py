def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    print(is_leap_year(400))
    print(is_leap_year(100))
    print(is_leap_year(2004))
    print(is_leap_year(2001))
    print(is_leap_year(2000))