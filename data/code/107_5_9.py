from datetime import datetime, timezone

def format_date_with_timezone(date_object):
    if not isinstance(date_object, datetime):
        raise ValueError("Input must be a datetime object")
    
    offset = date_object.utcoffset()
    hours = abs(offset.total_seconds() // 3600)
    minutes = abs((offset.total_seconds() % 3600) // 60)
    sign = '+' if offset.total_seconds() >= 0 else '-'
    return f"{sign}{hours:02d}{minutes:02d}"

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30, tzinfo=timezone.utc)
    formatted_date = format_date_with_timezone(sample_date)
    print(f"Input: {sample_date}, Result: {formatted_date}")