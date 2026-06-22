from datetime import date, timedelta

def next_weekend_date():
    today = date.today()
    days_ahead = 7 - today.weekday()
    if days_ahead == 0:
        days_ahead = 7
    next_weekend = today + timedelta(days=days_ahead)
    return next_weekend

if __name__ == '__main__':
    result = next_weekend_date()
    print(result)