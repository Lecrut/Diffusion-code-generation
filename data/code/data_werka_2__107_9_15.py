import calendar

def format_date(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Date string must have exactly three parts separated by hyphens")
    year_str, month_str, day_str = parts
    if not year_str.isdigit() or len(year_str) != 4:
        raise ValueError("Year must be a 4-digit number")
    if not month_str.isdigit() or not (1 <= int(month_str) <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not day_str.isdigit():
        raise ValueError("Day must be a number")
    year = int(year_str)
    month = int(month_str)
    day = int(day_str)
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31")
    month_name = calendar.month_name[month]
    return f"{month_name} {day:02d}, {year}"

if __name__ == '__main__':
    print(format_date('2023-1-5'))
    print(format_date('2024-12-25'))
    print(format_date('2000-2-29'))