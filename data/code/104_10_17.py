import datetime

def compare_dates(date1: datetime.date, date2: datetime.date) -> int:
    if not isinstance(date1, datetime.date):
        raise ValueError('First argument must be a datetime.date object')
    if not isinstance(date2, datetime.date):
        raise ValueError('Second argument must be a datetime.date object')
    if date1 > date2:
        return 1
    elif date1 < date2:
        return -1
    else:
        return 0
if __name__ == '__main__':
    date_a = datetime.date(2023, 10, 5)
    date_b = datetime.date(2023, 9, 15)
    result = compare_dates(date_a, date_b)
    print(result)