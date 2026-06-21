def is_leap_year(year):
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0
    is_leap = divisible_by_400 or (divisible_by_4 and not divisible_by_100)
    return is_leap

if __name__ == '__main__':
    result_2020 = is_leap_year(2020)
    result_2001 = is_leap_year(2001)
    result_1600 = is_leap_year(1600)
    result_1700 = is_leap_year(1700)
    print(result_2020)
    print(result_2001)
    print(result_1600)
    print(result_1700)