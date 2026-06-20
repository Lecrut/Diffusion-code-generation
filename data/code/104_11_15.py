import datetime

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    d2 = datetime.datetime(2023, 10, 25, 15, 45, 0)
    d3 = datetime.datetime(2024, 1, 1, 0, 0, 0)
    d4 = datetime.datetime(2024, 1, 1, 0, 0, 0)
    
    print(days_between_dates(d1, d2))
    print(days_between_dates(d3, d4))
    print(days_between_dates(d2, d1))
    print(days_between_dates(d4, d3))
    print(days_between_dates(d1, d1))