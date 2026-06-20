import datetime

weekdays = {0: False, 1: True, 2: True, 3: True, 4: True}

def is_weekday(dt: datetime.datetime) -> bool:
    return weekdays[dt.weekday()]

if __name__ == '__main__':
    date1 = datetime.datetime(2023, 10, 25)
    date2 = datetime.datetime(2023, 10, 26)
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")