from datetime import datetime
import calendar

def get_day_of_month(dt: datetime) -> int:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    if dt.day < 1 or dt.day > calendar.monthrange(dt.year, dt.month)[1]:
        raise ValueError("Invalid day for the given month and year")
    return dt.day

if __name__ == '__main__':
    sample_date = datetime(2024, 2, 29)
    day_value = get_day_of_month(sample_date)
    print(day_value)