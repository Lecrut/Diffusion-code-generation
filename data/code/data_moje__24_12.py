is_leap = lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

if __name__ == '__main__':
    test_years = [1600, 1700, 1800, 1900, 1996, 2000, 2004, 2019, 2020, 2100]
    for year in test_years:
        print(year, is_leap(year))