is_leap = lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 1600, 1700, 2004, 1901]
    results = {year: is_leap(year) for year in test_years}
    print(results)