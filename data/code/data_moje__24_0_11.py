def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    test_cases = [2000, 1900, 2024, 2023, 2400, 2100, 2020, 2019, 1600, 1700]
    for year in test_cases:
        print(is_leap_year(year))