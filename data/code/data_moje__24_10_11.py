def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 1600, 1700, 2004, 2100]
    results = [is_leap_year(year) for year in test_years]
    print(results)