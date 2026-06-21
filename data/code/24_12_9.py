is_leap = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
if __name__ == "__main__":
    test_years = [1600, 1700, 1800, 1900, 2000, 2020, 2021, 2024, 2100]
    results = [is_leap(year) for year in test_years]
    print(results)