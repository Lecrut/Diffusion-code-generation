from datetime import datetime

def validate_datetime_format(date_string):
    try:
        datetime.strptime(date_string, '%m/%d/%y')
        return True
    except ValueError:
        return False

def format_date_with_timezone(date_string):
    if not validate_datetime_format(date_string):
        raise ValueError("Invalid date string format. Expected MM/DD/YY")
    
    dt = datetime.strptime(date_string, '%m/%d/%y')
    tz_offset = dt.utcoffset()
    tz_hours = abs(tz_offset.total_seconds() // 3600)
    tz_minutes = (abs(tz_offset.total_seconds()) % 3600) // 60
    tz_sign = '+' if tz_offset.days >= 0 else '-'
    
    return f"{tz_sign}{tz_hours:02d}{tz_minutes:02d}"

if __name__ == '__main__':
    date_str_valid = "03/15/23"
    result = format_date_with_timezone(date_str_valid)
    print(f"Input: {date_str_valid}, Result: {result}")