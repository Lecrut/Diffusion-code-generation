import datetime

def days_between(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 1)
    d2 = datetime.date(2023, 1, 15)
    print(days_between(d1, d2))