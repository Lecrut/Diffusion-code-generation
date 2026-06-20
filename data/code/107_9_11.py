import calendar

def format_date_string(date_string):
    try:
        year, month, day = map(int, date_string.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError("Invalid date range")
        return f"{calendar.month_name[month]} {day}, {year}"
    except (ValueError, AttributeError) as e:
        return "Invalid date format"

if __name__ == '__main__':
    date1 = "2023-10-05"
    date2 = "2024-01-31"
    date3 = "1999-12-01"
    print(format_date_string(date1))
    print(format_date_string(date2))
    print(format_date_string(date3))