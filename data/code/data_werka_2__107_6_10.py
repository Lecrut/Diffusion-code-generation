from datetime import datetime
from calendar import day_name, month_name

def format_date_into_custom_style(d: datetime) -> str:
    if not isinstance(d, datetime):
        raise ValueError("Input must be a datetime instance")
    
    if d.year < 1 or d.year > 9999:
        raise ValueError("Year out of valid range")
    
    if d.month < 1 or d.month > 12:
        raise ValueError("Month out of valid range")
    
    try:
        d.timetuple()
    except (ValueError, OverflowError):
        raise ValueError("Date is not valid")
    
    day_name_str = day_name[d.weekday()]
    month_name_str = month_name[d.month]
    
    return f"{day_name_str}, {month_name_str} {d.day:02d}, {d.year}"

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 25)
    result = format_date_into_custom_style(sample_date)
    print(result)