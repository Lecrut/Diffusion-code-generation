from datetime import datetime, timedelta

def next_monday(date):
    days_ahead = (6 - date.weekday()) % 7 + 1
    return date + timedelta(days=days_ahead)

if __name__ == '__main__':
    sample_date = datetime(2023, 9, 10)
    result = next_monday(sample_date)
    print(result)