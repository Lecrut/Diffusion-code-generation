leap_year = lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2004, 1600]
    results = [(year, leap_year(year)) for year in test_years]
    print(results)