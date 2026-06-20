import datetime

def calculate_days_in_month(year, month):
    if month == 2:
        return 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def calculate_remaining_seconds_in_month():
    current_date = datetime.date.today()
    days_in_current_month = calculate_days_in_month(current_date.year, current_date.month)
    seconds_in_day = 24 * 60 * 60
    total_seconds_in_month = days_in_current_month * seconds_in_day
    seconds_passed_today = (current_date - current_date.replace(day=1)).days * seconds_in_day + datetime.datetime.now().hour * 3600 + datetime.datetime.now().minute * 60 + datetime.datetime.now().second
    return total_seconds_in_month - seconds_passed_today

if __name__ == '__main__':
    print(calculate_remaining_seconds_in_month())