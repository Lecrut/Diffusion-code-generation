import datetime

def calculate_day_difference(date1, date2):
    return abs((date1 - date2).days)

if __name__ == '__main__':
    d1 = datetime.datetime(2023, 11, 15, 14, 0, 0)
    d2 = datetime.datetime(2023, 11, 10, 9, 0, 0)
    print(calculate_day_difference(d1, d2))