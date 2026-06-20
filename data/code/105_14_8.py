from datetime import datetime, timedelta

def next_monday():
    today = datetime.now()
    days_until_monday = (7 - today.weekday()) % 7
    return today + timedelta(days=days_until_monday)

if __name__ == '__main__':
    print(next_monday().strftime('%Y-%m-%d'))