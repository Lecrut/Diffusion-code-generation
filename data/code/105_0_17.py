from datetime import datetime, timedelta

def next_monday():
    today = datetime.now()
    days_until_monday = (7 - today.weekday()) % 7
    next_monday_date = today + timedelta(days=days_until_monday)
    return next_monday_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(next_monday())