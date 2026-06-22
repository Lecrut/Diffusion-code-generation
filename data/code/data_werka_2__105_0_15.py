import datetime

def get_next_monday():
    today = datetime.date.today()
    days_ahead = (7 - today.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    next_monday = today + datetime.timedelta(days=days_ahead)
    return next_monday

if __name__ == '__main__':
    result = get_next_monday()
    print(result)