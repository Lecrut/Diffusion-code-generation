import datetime
import calendar

def format_hardcoded_date(date_string):
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    parts = date_string.split('/')
    if len(parts) != 3:
        raise ValueError("Date format must be YYYY/MM/DD")
    year, month, day = (int(p) for p in parts)
    if month < 1 or month > 12:
        raise ValueError("Invalid month")
    max_day = calendar.monthrange(year, month)[1]
    if day < 1 or day > max_day:
        raise ValueError("Invalid day for month")
    month_name = calendar.month_name[month]
    return f"{month_name} {day:02d}, {year}"

if __name__ == '__main__':
    sample_date = '2023/10/05'
    formatted = format_hardcoded_date(sample_date)
    print(formatted)