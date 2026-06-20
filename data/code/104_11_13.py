import datetime

def days_difference(date1, date2):
    if not date1.tzinfo and not date2.tzinfo:
        return abs((date1 - date2).days)
    else:
        raise ValueError("Date objects must be timezone-naive or have the same timezone.")

if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    d2 = datetime.datetime(2023, 10, 25, 15, 45, 0)
    print(days_difference(d1, d2))