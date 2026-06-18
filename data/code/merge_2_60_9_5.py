def is_leap_year(year):
    if year <= 0:
        return False
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, -5]
    for year in test_years:
        print(f"{year}: {is_leap_year(year)}")