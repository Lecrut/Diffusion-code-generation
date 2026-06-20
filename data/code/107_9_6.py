import calendar

def format_date_string(date_string):
    try:
        year, month, day = map(int, date_string.split('-'))
        month_name = calendar.month_name[month]
        return f"{month_name} {day}, {year}"
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    date1 = "2023-05-15"
    date2 = "2024-11-30"
    date3 = "2022-07-04"
    print(format_date_string(date1))
    print(format_date_string(date2))
    print(format_date_string(date3))