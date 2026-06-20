import datetime

def find_next_weekend():
    today = datetime.date.today()
    days_until_weekend = (5 - today.weekday()) % 7 + 1 if today.weekday() < 5 else 2
    next_weekend = today + datetime.timedelta(days=days_until_weekend)
    return next_weekend

if __name__ == '__main__':
    result = find_next_weekend()
    print(f"Next Weekend Date: {result}")