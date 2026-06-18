def is_leap_year(year):
    if not isinstance(year, int) and year != "":
        return False
    try:
        y = int(year)
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            return True
        else:
            return False
    except ValueError:
        return False
if __name__ == '__main__':
    test_years = [2000, 1900, 2024, "abc", -5]
    for year in test_years:
        result = is_leap_year(year)
        print(f"Year {year}: {'Leap' if result else 'Not Leap'}")