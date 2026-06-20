import datetime

def find_next_monday():
    today = datetime.date.today()
    days_until_monday = (7 - today.weekday()) % 7
    return today + datetime.timedelta(days=days_until_monday)

if __name__ == '__main__':
    next_monday_date = find_next_monday()
    print(next_monday_date.strftime("%Y-%m-%d"))