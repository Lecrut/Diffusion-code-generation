def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    test_years = [2000, 2004, 2008, 2100]
    for y in test_years:
        result = "Leap Year" if is_leap_year(y) else "Not a Leap Year"
        print(f"{y}: {result}")