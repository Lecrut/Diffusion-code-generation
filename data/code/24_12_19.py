is_leap = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def validate_leap_years():
    leap_years = [4, 8, 2000, 2004, 2400]
    non_leap_years = [3, 100, 1800, 1900, 2100, 2200, 2300]
    results = {year: is_leap(year) for year in leap_years + non_leap_years}
    return results

if __name__ == '__main__':
    output = validate_leap_years()
    for year, is_leap_result in sorted(output.items()):
        print(f"{year}: {is_leap_result}")