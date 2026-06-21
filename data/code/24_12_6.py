is_leap = lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

if __name__ == '__main__':
    years = [1600, 1700, 1800, 1900, 2000, 2024, 2023]
    results = [(year, is_leap(year)) for year in years]
    print(results)