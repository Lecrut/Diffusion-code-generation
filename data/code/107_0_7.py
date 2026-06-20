from datetime import datetime

def is_valid_datetime_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

def format_datetime_to_iso(dt):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    return dt.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    formatted_date = format_datetime_to_iso(sample_dt)
    print(formatted_date)