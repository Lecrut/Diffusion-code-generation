import datetime

def is_weekday(date_obj: datetime.date) -> bool:
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Input must be a datetime.date object")
    return 0 <= date_obj.weekday() < 5

if __name__ == '__main__':
    sample_date1 = datetime.date(2023, 10, 24)
    sample_date2 = datetime.date(2023, 10, 27)
    print(f"Is {sample_date1} a weekday? {is_weekday(sample_date1)}")
    print(f"Is {sample_date2} a weekday? {is_weekday(sample_date2)}")