is_leap = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 1600, 1700, 2004, 1999, 2100, 2400]
    for year in test_years:
        print(f"{year}: {is_leap(year)}")