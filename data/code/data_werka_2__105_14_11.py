import datetime

def next_monday():
    today = datetime.date.today()
    days_ahead = (7 - today.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    next_monday_date = today + datetime.timedelta(days=days_ahead)
    return next_monday_date

if __name__ == '__main__':
    result = next_monday()
    print(result)