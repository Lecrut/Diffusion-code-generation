from datetime import datetime

def format_datetime_to_iso(dt):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be an instance of datetime")
    return dt.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    formatted_date = format_datetime_to_iso(sample_dt)
    print(formatted_date)