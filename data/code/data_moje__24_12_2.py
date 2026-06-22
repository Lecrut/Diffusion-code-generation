is_leap_year = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

if __name__ == '__main__':
    leap_years = [1600, 2000, 2004, 2008, 2012, 2016, 2020, 2024]
    non_leap_years = [1700, 1800, 1900, 2001, 2002, 2003, 2005, 2019, 2023]

    for y in leap_years:
        print(f"{y}: {is_leap_year(y)}")
    for y in non_leap_years:
        print(f"{y}: {is_leap_year(y)}")