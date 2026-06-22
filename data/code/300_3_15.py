from datetime import date, timedelta
DAYS_IN_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def days_left_in_month():
    today = date.today()
    if today.month == 2:
        is_leap = today.year % 4 == 0 and today.year % 100 != 0 or today.year % 400 == 0
        last_day_of_month = DAYS_IN_MONTH[2] + is_leap
    else:
        last_day_of_month = DAYS_IN_MONTH[today.month]
    last_day_of_current_month = date(today.year, today.month, last_day_of_month)
    return (last_day_of_current_month - today).days
if __name__ == '__main__':
    result = days_left_in_month()
    print(result)