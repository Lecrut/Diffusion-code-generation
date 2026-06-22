from datetime import datetime

def format_datetime_iso8601(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime(2024, 1, 15, 9, 5, 30)
    formatted = format_datetime_iso8601(sample_dt)
    print(formatted)