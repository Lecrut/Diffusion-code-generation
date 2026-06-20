import datetime

def is_weekday(date):
    return date.weekday() < 5
if __name__ == '__main__':
    sample_date = datetime.date(2023, 4, 14)
    print(is_weekday(sample_date))