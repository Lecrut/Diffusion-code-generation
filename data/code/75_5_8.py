import datetime

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 1)
    date2 = datetime.date(2023, 10, 15)
    print(days_between_dates(date1, date2))