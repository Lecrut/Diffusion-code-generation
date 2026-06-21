import calendar

def format_date(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Date string must contain three parts")
    year_str, month_str, day_str = parts
    if not year_str.isdigit() or not month_str.isdigit() or not day_str.isdigit():
        raise ValueError("Date parts must be numeric")
    year = int(year_str)
    month = int(month_str)
    day = int(day_str)
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12")
    month_name = calendar.month_name[month]
    return f"{month_name} {day:02d}, {year}"

if __name__ == '__main__':
    print(format_date('2023-1-5'))
    print(format_date('2024-12-25'))
    print(format_date('2000-2-29'))