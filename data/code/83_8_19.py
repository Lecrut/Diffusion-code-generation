import datetime

def are_same_day(date1: datetime.datetime, date2: datetime.datetime) -> bool:
    if not isinstance(date1, datetime.datetime) or not isinstance(date2, datetime.datetime):
        raise ValueError("Both inputs must be datetime objects.")
    return date1.date() == date2.date()

if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 15, 30)
    d2 = datetime.datetime(2023, 10, 26, 9, 45)
    d3 = datetime.datetime(2023, 11, 1, 10, 0)
    d4 = datetime.datetime(2023, 10, 25, 18, 30)

    print(f"Are {d1} and {d2} on the same day? {are_same_day(d1, d2)}")
    print(f"Are {d1} and {d3} on the same day? {are_same_day(d1, d3)}")
    print(f"Are {d3} and {d1} on the same day? {are_same_day(d3, d1)}")
    print(f"Are {d4} and {d1} on the same day? {are_same_day(d4, d1)}")