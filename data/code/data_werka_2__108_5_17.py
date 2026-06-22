from datetime import datetime
import calendar

def get_day_of_month(dt: datetime) -> int:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    if dt.year < 1 or dt.year > 9999:
        raise ValueError("Year out of valid range")
    if dt.month < 1 or dt.month > 12:
        raise ValueError("Month out of valid range")
    max_day = calendar.monthrange(dt.year, dt.month)[1]
    if dt.day < 1 or dt.day > max_day:
        raise ValueError("Day out of valid range for the given month/year")
    return dt.day

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    result = get_day_of_month(sample_date)
    print(result)