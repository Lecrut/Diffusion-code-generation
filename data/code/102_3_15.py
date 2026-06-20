import datetime

def is_weekday(date):
    return date.weekday() < 5

if __name__ == '__main__':
    test_date = datetime.date(2023, 10, 26)
    print(is_weekday(test_date))