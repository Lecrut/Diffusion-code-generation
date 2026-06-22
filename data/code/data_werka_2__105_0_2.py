from datetime import datetime, timedelta

def get_next_monday():
    today = datetime.today()
    days_ahead = 0
    if today.weekday() < 1:
        days_ahead = 1 - today.weekday()
    else:
        days_ahead = 8 - today.weekday()
    next_monday = today + timedelta(days=days_ahead)
    return next_monday

if __name__ == '__main__':
    result = get_next_monday()
    print(result.strftime('%Y-%m-%d'))