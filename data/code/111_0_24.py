from datetime import date

DAYS_IN_NON_LEAP_YEAR = 365
DAYS_IN_LEAP_YEAR = 366
JANUARY = 1
LAST_DAY_OF_YEAR = 31
TARGET_YEAR = 2023

def determine_days_for_year(year):
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if is_leap:
        return DAYS_IN_LEAP_YEAR
    return DAYS_IN_NON_LEAP_YEAR

def calculate_full_year_days(year):
    start_date = date(year, JANUARY, 1)
    end_date = date(year, 12, LAST_DAY_OF_YEAR)
    delta = end_date - start_date
    return delta.days + 1

if __name__ == '__main__':
    days = calculate_full_year_days(TARGET_YEAR)
    print(days)