import calendar

MONTH_NAMES = calendar.month_name
DATE_SEPARATOR = '-'
OUTPUT_MONTH_INDEX_OFFSET = 1
MIN_YEAR = 1
MAX_YEAR = 9999
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

def parse_and_format_date(date_string):
    if not isinstance(date_string, str):
        raise TypeError("Input must be a string")
    
    parts = date_string.split(DATE_SEPARATOR)
    
    if len(parts) != 3:
        raise ValueError("Date string must contain exactly three parts separated by hyphens")
    
    year_str, month_str, day_str = parts
    
    try:
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
    except ValueError:
        raise ValueError("Year, month, and day must be integers")
    
    if not (MIN_YEAR <= year <= MAX_YEAR):
        raise ValueError(f"Year must be between {MIN_YEAR} and {MAX_YEAR}")
    
    if not (MIN_MONTH <= month <= MAX_MONTH):
        raise ValueError(f"Month must be between {MIN_MONTH} and {MAX_MONTH}")
    
    if not (MIN_DAY <= day <= MAX_DAY):
        raise ValueError(f"Day must be between {MIN_DAY} and {MAX_DAY}")
    
    month_name = MONTH_NAMES[month + OUTPUT_MONTH_INDEX_OFFSET]
    
    formatted_day = f"{day:02d}"
    formatted_year = f"{year:04d}"
    
    return f"{month_name} {formatted_day}, {formatted_year}"

if __name__ == '__main__':
    test_dates = [
        '2023-1-5',
        '2024-12-25',
        '2000-2-29',
        '1999-7-1',
        '2021-11-11'
    ]
    
    for date_input in test_dates:
        result = parse_and_format_date(date_input)
        print(result)