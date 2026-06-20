def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    sample_years = [1984, 2000, 2016, 1900, 2023]
    for year in sample_years:
        print(f"Year {year}: {is_leap_year(year)}")