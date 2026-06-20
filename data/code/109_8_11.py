from datetime import date, timedelta

def weekdays_left_in_month():
    today = date.today()
    last_day_of_month = date(today.year, today.month + 1, 1) - timedelta(days=1)
    weekdays_count = sum(1 for day in range((last_day_of_month - today).days + 1) if (today + timedelta(days=day)).weekday() < 5)
    return weekdays_count

if __name__ == '__main__':
    print(weekdays_left_in_month())