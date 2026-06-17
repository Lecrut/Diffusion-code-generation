from datetime import datetime
def is_weekend(dt: datetime) -> bool:
    return dt.weekday() >= 5
if __name__ == '__main__':
    date1 = datetime(2023, 10, 1)
    date2 = datetime(2023, 10, 7)
    date3 = datetime(2023, 10, 8)
    print(f"Is {date1.date()} a weekend? {is_weekend(date1)}")
    print(f"Is {date2.date()} a weekend? {is_weekend(date2)}")
    print(f"Is {date3.date()} a weekend? {is_weekend(date3)}")