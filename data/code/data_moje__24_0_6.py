def is_leap_year(year):
    century_check = year % 100 == 0
    quad_check = year % 4 == 0
    quad_century_check = year % 400 == 0
    is_divisible_by_4 = quad_check and not century_check
    is_divisible_by_400 = quad_century_check
    return is_divisible_by_4 or is_divisible_by_400

if __name__ == '__main__':
    print(is_leap_year(1600))
    print(is_leap_year(1700))
    print(is_leap_year(2004))
    print(is_leap_year(1896))