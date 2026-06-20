import datetime

def days_in_month(year, month):
    if month == 2:
        return 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def calculate_seconds_remaining_in_current_month():
    current_date = datetime.date.today()
    days_left = days_in_month(current_date.year, current_date.month) - current_date.day + 1
    seconds_per_day = 24 * 60 * 60
    total_seconds_remaining = days_left * seconds_per_day
    return total_seconds_remaining

if __name__ == '__main__':
    result = calculate_seconds_remaining_in_current_month()
    print(result)