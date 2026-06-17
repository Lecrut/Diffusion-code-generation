def is_leap_year(year):
    return (year % 400 == 0) and ((year % 100 != 0) or (year % 4 == 0))
if __name__ == '__main__':
    test_years = [2000, 2004, 2001, 1900]
    for year in test_years:
        print(f"{year}: {is_leap_year(year)}")