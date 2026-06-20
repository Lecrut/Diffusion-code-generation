import calendar

def parse_and_format_date(date_string):
    try:
        year, month, day = map(int, date_string.split('-'))
        if not (1 <= month <= 12) or not (1 <= day <= 31):
            raise ValueError("Invalid date format")
        return f"{calendar.month_name[month]} {day}, {year}"
    except (ValueError, TypeError):
        return "Invalid date format"

if __name__ == '__main__':
    date1 = "2023-10-05"
    date2 = "2024-01-31"
    date3 = "2022-12-01"
    print(parse_and_format_date(date1))
    print(parse_and_format_date(date2))
    print(parse_and_format_date(date3))