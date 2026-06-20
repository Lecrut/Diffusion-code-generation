import calendar

def format_date_string(date_string):
    try:
        year, month, day = map(int, date_string.split('-'))
        month_name = calendar.month_name[month]
        return f"{month_name} {day}, {year}"
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    date1 = "2023-10-05"
    date2 = "2024-01-31"
    date3 = "2022-12-01"
    print(format_date_string(date1))
    print(format_date_string(date2))
    print(format_date_string(date3))