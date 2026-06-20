from dateutil.relativedelta import relativedelta

def is_within_one_week(date1, date2):
    return abs((date1 - date2).days) <= 7

if __name__ == '__main__':
    from datetime import datetime
    date1 = datetime(2023, 4, 1)
    date2 = datetime(2023, 4, 8)
    print(is_within_one_week(date1, date2))