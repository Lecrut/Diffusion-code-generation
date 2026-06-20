from datetime import datetime

def parse_datetime(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format")

def compare_datetimes_ignoring_time(dt1, dt2):
    if not isinstance(dt1, datetime) or not isinstance(dt2, datetime):
        raise TypeError("Inputs must be datetime objects")
    
    return dt1.date() == dt2.date()

if __name__ == '__main__':
    try:
        date_str1 = "2023-10-27"
        date_str2 = "2023-10-27"
        
        dt1 = parse_datetime(date_str1)
        dt2 = parse_datetime(date_str2)
        
        result = compare_datetimes_ignoring_time(dt1, dt2)
        
        print("The dates are the same" if result else "The dates are different")
    except (ValueError, TypeError) as e:
        print(e)