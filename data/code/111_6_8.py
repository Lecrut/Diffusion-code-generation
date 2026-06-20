from datetime import datetime, timedelta

def next_monday(date):
    days_until_monday = (7 - date.weekday()) % 7
    return date + timedelta(days=days_until_monday)

if __name__ == '__main__':
    sample_date = datetime(2023, 9, 10)
    print(next_monday(sample_date))