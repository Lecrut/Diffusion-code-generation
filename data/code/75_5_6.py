import datetime

def days_between(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 12, 31)
    print(days_between(date1, date2))