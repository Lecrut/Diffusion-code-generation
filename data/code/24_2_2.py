def is_leap_year(year): return bool(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

if __name__ == '__main__':
    print(is_leap_year(2024))
    print(is_leap_year(1900))
    print(is_leap_year(2000))