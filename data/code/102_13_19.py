import datetime

weekday_map = {
    0: False,
    1: True,
    2: True,
    3: True,
    4: True,
    5: False,
    6: False
}

def is_weekday(dt: datetime.datetime) -> bool:
    return weekday_map[dt.weekday()]

if __name__ == '__main__':
    date1 = datetime.datetime(2023, 10, 25)
    date2 = datetime.datetime(2023, 10, 26)
    date3 = datetime.datetime(2023, 10, 27)
    date4 = datetime.datetime(2023, 10, 28)
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")