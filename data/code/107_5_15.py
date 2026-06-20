from datetime import datetime, timezone

def format_datetime_with_timezone(date_time):
    try:
        if isinstance(date_time, str):
            date_object = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        elif isinstance(date_time, datetime):
            date_object = date_time
        else:
            raise ValueError("Invalid input type. Expected string or datetime object.")
        
        utc_offset = date_object.astimezone(timezone.utc).utcoffset()
        offset_minutes = abs(utc_offset.total_seconds() // 60)
        sign = '+' if utc_offset.total_seconds() > 0 else '-'
        return f"{date_object:%Y-%m-%d %H:%M:%S}{sign}{offset_minutes:02d}00"
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    date_str_valid = "2023-04-15 12:34:56"
    result_valid = format_datetime_with_timezone(date_str_valid)
    print(f"Input: {date_str_valid}, Result: {result_valid}")

    date_dt_valid = datetime(2023, 4, 15, 12, 34, 56)
    result_dt_valid = format_datetime_with_timezone(date_dt_valid)
    print(f"Input: {date_dt_valid}, Result: {result_dt_valid}")