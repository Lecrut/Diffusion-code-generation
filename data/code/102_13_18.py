import datetime

def is_valid_date(date_obj):
    if not isinstance(date_obj, datetime.datetime):
        raise ValueError("Provided object is not an instance of datetime.datetime")
    return True

def is_weekday(dt: datetime.datetime) -> bool:
    if not is_valid_date(dt):
        raise ValueError("Invalid date provided")
    return dt.weekday() < 5

if __name__ == '__main__':
    date1 = datetime.datetime(2023, 10, 25)
    date2 = datetime.datetime(2023, 10, 26)
    date3 = datetime.datetime(2023, 10, 27)
    date4 = datetime.datetime(2023, 10, 28)
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")