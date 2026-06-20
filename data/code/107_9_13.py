import datetime

def parse_and_format_date(date_string):
    if not isinstance(date_string, str) or len(date_string) != 10:
        raise ValueError("Invalid date format")
    
    parts = date_string.split('-')
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        raise ValueError("Invalid date format")
    
    year, month, day = map(int, parts)
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        raise ValueError("Invalid date format")
    
    return f"{month} {day}, {year}"

if __name__ == '__main__':
    date1 = "2023-10-05"
    date2 = "2024-01-31"
    date3 = "2022-12-01"
    
    print(parse_and_format_date(date1))
    print(parse_and_format_date(date2))
    print(parse_and_format_date(date3))