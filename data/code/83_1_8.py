from datetime import datetime

def parse_datetime(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'.")

def compare_datetimes_ignoring_time(dt1, dt2):
    if not isinstance(dt1, datetime) or not isinstance(dt2, datetime):
        raise TypeError("Both arguments must be instances of datetime.datetime.")
    return dt1.date() == dt2.date()

if __name__ == '__main__':
    dt_str1 = "2023-10-27 14:30:00"
    dt_str2 = "2023-10-27 19:45:00"
    
    dt1 = parse_datetime(dt_str1)
    dt2 = parse_datetime(dt_str2)
    
    result = compare_datetimes_ignoring_time(dt1, dt2)
    print(result)