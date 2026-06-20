import datetime

WEEKDAY_THRESHOLD = 5

def is_weekday(date):
    return date.weekday() < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 25)
    print(is_weekday(sample_date))