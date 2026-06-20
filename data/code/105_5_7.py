from datetime import datetime, timedelta

def next_wednesday(date):
    days_until_wednesday = (2 - date.weekday()) % 7
    return date + timedelta(days=days_until_wednesday)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 10)
    print(next_wednesday(sample_date).strftime("%Y-%m-%d"))