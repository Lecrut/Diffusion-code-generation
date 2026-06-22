is_leap = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2400, 1800]
    for year in test_years:
        print(f"{year}: {is_leap(year)}")