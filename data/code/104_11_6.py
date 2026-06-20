import datetime

def days_difference(dt1, dt2):
    return abs((dt1 - dt2).days)

if __name__ == '__main__':
    dt1 = datetime.datetime(2023, 10, 1)
    dt2 = datetime.datetime(2023, 9, 15)
    print(days_difference(dt1, dt2))