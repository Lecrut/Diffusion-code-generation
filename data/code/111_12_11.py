def count_leap_years(start_year, end_year):
    is_leap = lambda year: (year & 3 == 0) and ((year % 100 != 0) or (year & 399 == 0))
    return sum(is_leap(year) for year in range(start_year, end_year + 1))

if __name__ == '__main__':
    print(count_leap_years(2000, 2020))