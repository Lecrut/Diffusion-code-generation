import datetime

def find_next_weekend():
    today = datetime.date.today()
    days_ahead = (5 - today.weekday()) % 7 + 1 if today.weekday() < 5 else 2
    next_weekend_date = today + datetime.timedelta(days=days_ahead)
    return next_weekend_date

if __name__ == '__main__':
    result = find_next_weekend()
    print(f"Next Weekend Date: {result}")