from datetime import datetime, timedelta

def next_monday(timestamp):
    target_date = datetime.strptime('2024-02-28', '%Y-%m-%d')
    days_until_monday = (7 - (target_date.weekday() + 1)) % 7
    return target_date + timedelta(days=days_until_monday)

if __name__ == '__main__':
    print(next_monday(None))