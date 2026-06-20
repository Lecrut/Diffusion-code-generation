import datetime

def days_in_month(year, month):
    if month == 2:
        return 28 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def total_seconds_in_year(year):
    total_seconds = 0
    for month in range(1, 13):
        total_seconds += days_in_month(year, month) * 24 * 60 * 60
    return total_seconds

if __name__ == '__main__':
    year = 2023
    print(f"Total seconds in {year}: {total_seconds_in_year(year)}")