import datetime

def find_next_monday():
    today = datetime.date.today()
    days_until_monday = (7 - today.weekday()) % 7
    return today + datetime.timedelta(days=days_until_monday)
if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    next_monday = find_next_monday()
    print(next_monday.strftime('%Y-%m-%d'))