from datetime import datetime, timedelta

def next_weekend():
    today = datetime.now()
    days_until_weekend = (5 - today.weekday()) % 7 + 2
    return today + timedelta(days=days_until_weekend)

if __name__ == '__main__':
    print(next_weekend())