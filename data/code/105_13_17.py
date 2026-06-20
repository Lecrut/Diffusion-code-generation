from datetime import datetime, timedelta

def next_weekend():
    today = datetime.now()
    days_to_add = (5 - today.weekday()) % 7 + 2
    return today + timedelta(days=days_to_add)

if __name__ == '__main__':
    print(next_weekend())