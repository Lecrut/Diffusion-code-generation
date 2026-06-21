def is_leap_year(year: int) -> bool:
    return not year % 4 and (year % 100 or not year % 400)

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(2001))
    print(is_leap_year(2024))
    print(is_leap_year(1900))