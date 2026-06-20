import calendar

def is_valid_date(date_string):
    try:
        year, month, day = map(int, date_string.split('-'))
        return 1 <= month <= 12 and 1 <= day <= calendar.monthrange(year, month)[1]
    except ValueError:
        return False

def format_date_string(date_string):
    if not is_valid_date(date_string):
        return "Invalid date format"
    
    year, month, day = map(int, date_string.split('-'))
    month_name = calendar.month_name[month]
    formatted_date = f"{month_name} {day}, {year}"
    return formatted_date

if __name__ == '__main__':
    date1 = "2023-10-05"
    date2 = "2024-01-31"
    date3 = "1999-12-01"
    print(format_date_string(date1))
    print(format_date_string(date2))
    print(format_date_string(date3))