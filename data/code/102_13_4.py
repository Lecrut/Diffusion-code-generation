import datetime

def is_weekday(dt: datetime.datetime) -> bool:
    return 0 <= dt.weekday() < 5

if __name__ == '__main__':
    sample_date1 = datetime.datetime(2023, 10, 24)
    sample_date2 = datetime.datetime(2023, 10, 29)
    print(f"Is {sample_date1} a weekday? {is_weekday(sample_date1)}")
    print(f"Is {sample_date2} a weekday? {is_weekday(sample_date2)}")