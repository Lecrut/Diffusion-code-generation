is_leap = lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

if __name__ == '__main__':
    leap_years = [2000, 2024, 400]
    non_leap_years = [1900, 2019, 2100]
    print(list(map(is_leap, leap_years + non_leap_years)))