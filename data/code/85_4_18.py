import datetime

def week_difference(date1, date2):
    delta = abs((date2 - date1).days)
    return delta // 7
if __name__ == '__main__':
    print(week_difference(datetime.date(2023, 1, 1), datetime.date(2023, 1, 8)))
    print(week_difference(datetime.date(2023, 1, 8), datetime.date(2023, 1, 1)))
    print(week_difference(datetime.date(2023, 1, 1), datetime.date(2023, 2, 1)))
    print(week_difference(datetime.date(2023, 12, 31), datetime.date(2024, 1, 1)))