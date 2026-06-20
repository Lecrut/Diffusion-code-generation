import datetime

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def get_day_of_year(year, month, day):
    if not (1 <= month <= 12 and 1 <= day <= days_in_month(year, month)):
        raise ValueError("Invalid date")
    
    day_of_year = sum(days_in_month(year, m) for m in range(1, month)) + day
    return day_of_year

if __name__ == '__main__':
    year1 = 2023
    month1 = 10
    day1 = 27
    result1 = get_day_of_year(year1, month1, day1)
    print(f"Day of the year for {year1}-{month1:02d}-{day1:02d} is: {result1}")