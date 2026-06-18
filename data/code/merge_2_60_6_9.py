import sys
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    start_year = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    end_year = int(sys.argv[2]) if len(sys.argv) > 2 else 2100
    leap_years = []
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            leap_years.append(year)
    print(f"Leap years between {start_year} and {end_year}:")
    print(leap_years)