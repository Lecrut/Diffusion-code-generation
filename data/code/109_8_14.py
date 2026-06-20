import datetime

def weekdays_left_in_month(year=2023, month=10):
    today = datetime.date(year, month, 1)
    first_day_of_next_month = today.replace(day=28) + datetime.timedelta(days=4)
    if month == 12:
        next_month = today.replace(year=year + 1, month=1, day=1)
    else:
        next_month = today.replace(month=month + 1, day=1)
    days_in_current_month = (next_month - today).days
    weekdays_count = sum(1 for _ in range(days_in_current_month) if (today + datetime.timedelta(days=_)).weekday() < 5)
    return weekdays_count

if __name__ == '__main__':
    year = 2023
    month = 10
    weekdays_left = weekdays_left_in_month(year, month)
    print(weekdays_left)