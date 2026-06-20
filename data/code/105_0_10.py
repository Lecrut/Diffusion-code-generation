import datetime

WEEKDAY_MONDAY = 0

def calculate_next_monday():
    today = datetime.date.today()
    days_until_monday = (WEEKDAY_MONDAY - today.weekday()) % 7
    return today + datetime.timedelta(days=days_until_monday)

if __name__ == '__main__':
    next_monday_date = calculate_next_monday()
    print(next_monday_date.strftime("%Y-%m-%d"))