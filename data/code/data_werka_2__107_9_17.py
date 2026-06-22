import calendar

def format_date(date_string):
    parts = date_string.split('-')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    month_name = calendar.month_name[month]
    return f"{month_name} {day:02d}, {year}"

if __name__ == '__main__':
    result = format_date('2023-10-5')
    print(result)
    result2 = format_date('1999-1-1')
    print(result2)