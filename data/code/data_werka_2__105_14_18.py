import datetime

def get_next_monday():
    today = datetime.date.today()
    days_until_monday = (7 - today.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    next_monday = today + datetime.timedelta(days=days_until_monday)
    return next_monday

if __name__ == '__main__':
    result = get_next_monday()
    print(result)