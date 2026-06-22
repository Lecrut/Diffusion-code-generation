import datetime

def next_monday():
    today = datetime.date.today()
    days_ahead = 0
    if today.weekday() == 0:
        days_ahead = 7
    else:
        days_ahead = (0 - today.weekday()) % 7
    return today + datetime.timedelta(days=days_ahead)

if __name__ == '__main__':
    result = next_monday()
    print(result)