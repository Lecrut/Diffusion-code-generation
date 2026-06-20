def is_leap_year(year):
    try:
        year = int(year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    except ValueError:
        raise ValueError("Input must be a valid integer")

if __name__ == '__main__':
    sample_years = [2000, 1900, 2020, 2021]
    for year in sample_years:
        print(f"Year {year}: {is_leap_year(year)}")