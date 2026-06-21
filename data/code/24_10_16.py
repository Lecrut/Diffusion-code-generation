def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 2004, 1999, 2000, 2100, 2400]
    results = [is_leap_year(y) for y in test_years]
    for year, result in zip(test_years, results):
        print(f"{year}: {result}")