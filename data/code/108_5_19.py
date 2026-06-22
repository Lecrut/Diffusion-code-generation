from datetime import datetime

def get_day_of_month(dt: datetime) -> int:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    if dt.day < 1 or dt.day > 31:
        raise ValueError("Invalid day for the given month")
    return dt.day

if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 5)
    result = get_day_of_month(sample_datetime)
    print(result)