from datetime import date
DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def get_day_of_year(year, month, day):
    if is_leap_year(year):
        DAYS_IN_MONTH[2] = 29
    else:
        DAYS_IN_MONTH[2] = 28
    day_of_year = sum(DAYS_IN_MONTH[:month]) + day
    return day_of_year
if __name__ == '__main__':
    year1 = 2023
    month1 = 10
    day1 = 27
    result1 = get_day_of_year(year1, month1, day1)
    print(f'Day of the year for {year1}-{month1:02d}-{day1:02d} is: {result1}')