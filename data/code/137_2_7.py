def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

if __name__ == '__main__':
    test_years = [2000, 1900, 2020, 2021]
    for year in test_years:
        print(f"{year}: {is_leap_year(year)}")