import datetime

DAY_OF_YEAR = 365
FEBRUARY_29 = 29

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_day_of_year(year, month, day):
    if month < 1 or month > 12:
        raise ValueError("Invalid month")
    if day < 1:
        raise ValueError("Invalid day")
    
    month_lengths = [31, is_leap_year(year) + FEBRUARY_29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > month_lengths[month - 1]:
        raise ValueError("Invalid day for the given month")
    
    return sum(month_lengths[:month - 1]) + day

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    try:
        day_of_year = calculate_day_of_year(year, month, day)
        print(f"The day of the year for {year}-{month}-{day} is: {day_of_year}")
    except ValueError as e:
        print(e)