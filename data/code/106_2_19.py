from datetime import datetime

def validate_datetime(dt: datetime) -> None:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")

def year_difference(date1: datetime, date2: datetime) -> int:
    validate_datetime(date1)
    validate_datetime(date2)
    return abs((date2.year - date1.year))

if __name__ == '__main__':
    date1 = datetime(2000, 5, 15)
    date2 = datetime(2023, 8, 20)
    difference = year_difference(date1, date2)
    print(difference)