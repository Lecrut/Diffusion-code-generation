from datetime import date

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def calculate_day_of_year(date_obj):
    day_of_year = 0
    for m in range(1, date_obj.month):
        day_of_year += days_in_month(m, date_obj.year)
    day_of_year += date_obj.day
    return day_of_year

if __name__ == '__main__':
    sample_date = date(2023, 4, 15)
    print(f"Date: {sample_date} -> Day of Year: {calculate_day_of_year(sample_date)}")