def is_leap_year(year):
    is_divisible_by_4 = year % 4 == 0
    is_divisible_by_100 = year % 100 == 0
    is_divisible_by_400 = year % 400 == 0
    if is_divisible_by_4:
        if is_divisible_by_100:
            return is_divisible_by_400
        else:
            return True
    else:
        return False
if __name__ == '__main__':
    year1 = 2020
    year2 = 1900
    year3 = 2000
    year4 = 2023
    result1 = is_leap_year(year1)
    result2 = is_leap_year(year2)
    result3 = is_leap_year(year3)
    result4 = is_leap_year(year4)
    print(f'Year {year1} is a leap year: {result1}')
    print(f'Year {year2} is a leap year: {result2}')
    print(f'Year {year3} is a leap year: {result3}')
    print(f'Year {year4} is a leap year: {result4}')