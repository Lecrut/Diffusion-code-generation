import datetime

def first_sunday_after_jan_1():
    start_date = datetime.date(2024, 1, 1)
    while start_date.weekday() != 6:
        start_date += datetime.timedelta(days=1)
    return start_date

if __name__ == '__main__':
    print(first_sunday_after_jan_1())