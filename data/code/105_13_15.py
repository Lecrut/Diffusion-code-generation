from datetime import date, timedelta

WEEKEND_DAYS = {5: "Saturday", 6: "Sunday"}

def get_next_weekend_date():
    today = date.today()
    weekday = today.weekday()
    if weekday in WEEKEND_DAYS:
        return today
    days_until_next_saturday = 5 - weekday
    next_saturday = today + timedelta(days=days_until_next_saturday)
    return next_saturday

if __name__ == '__main__':
    result = get_next_weekend_date()
    print(result)