from datetime import datetime

def extract_day(dt: datetime) -> int:
    year: int = dt.year
    month: int = dt.month
    day: int = dt.day
    return day

if __name__ == '__main__':
    target_datetime: datetime = datetime(2024, 2, 29, 14, 0, 0)
    computed_day: int = extract_day(target_datetime)
    print(computed_day)