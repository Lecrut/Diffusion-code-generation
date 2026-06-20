from datetime import datetime, timedelta

def next_weekend():
    today = datetime.now()
    days_ahead = (5 - today.weekday()) % 7 + 2
    return today + timedelta(days=days_ahead)

if __name__ == '__main__':
    print(next_weekend())