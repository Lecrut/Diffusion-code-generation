from datetime import datetime

def is_valid_datetime(date_obj):
    return isinstance(date_obj, datetime)

def format_datetime_to_iso(dt):
    if not is_valid_datetime(dt):
        raise ValueError("Invalid datetime object")
    return dt.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    formatted_date = format_datetime_to_iso(sample_dt)
    print(formatted_date)