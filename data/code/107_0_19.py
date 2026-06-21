from datetime import datetime

def format_datetime_iso(dt: datetime) -> str:
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

if __name__ == '__main__':
    sample_date = datetime(2024, 12, 31, 23, 59, 59)
    formatted_string = format_datetime_iso(sample_date)
    print(formatted_string)