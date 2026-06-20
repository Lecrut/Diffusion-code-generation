import datetime

def is_weekday(date_obj: datetime.datetime) -> bool:
    if not isinstance(date_obj, datetime.datetime):
        raise ValueError("Input must be a datetime object")
    return 0 <= date_obj.weekday() < 5

if __name__ == '__main__':
    sample_date1 = datetime.datetime(2023, 10, 25)
    sample_date2 = datetime.datetime(2023, 10, 26)
    print(f"Is {sample_date1} a weekday? {is_weekday(sample_date1)}")
    print(f"Is {sample_date2} a weekday? {is_weekday(sample_date2)}")