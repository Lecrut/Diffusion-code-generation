import datetime

def next_monday():
    today = datetime.date.today()
    days_until_monday = (7 - today.weekday()) % 7
    next_monday_date = today + datetime.timedelta(days=days_until_monday)
    return next_monday_date

if __name__ == '__main__':
    print(next_monday())