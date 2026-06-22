import datetime

def get_next_monday():
    today = datetime.date.today()
    days_ahead = 0
    if today.weekday() < 1:
        days_ahead = 1 - today.weekday()
    else:
        days_ahead = 8 - today.weekday()
    next_monday = today + datetime.timedelta(days=days_ahead)
    return next_monday

if __name__ == '__main__':
    result = get_next_monday()
    print(result)