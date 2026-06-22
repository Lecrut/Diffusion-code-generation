is_leap = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2400, 2100]
    results = {year: is_leap(year) for year in test_years}
    for year, leap in results.items():
        print(f"{year}: {leap}")