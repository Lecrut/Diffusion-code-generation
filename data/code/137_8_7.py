def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    return False

if __name__ == '__main__':
    years = [2000, 1900, 2020, 2023]
    for year in years:
        print(f"Year {year}: {is_leap_year(year)}")