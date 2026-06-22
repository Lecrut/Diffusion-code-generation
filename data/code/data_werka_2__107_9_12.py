import calendar

def parse_and_format_date(date_string):
    parts = date_string.split('-')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    month_name = calendar.month_name[month]
    formatted = f"{month_name} {day:02d}, {year}"
    return formatted

if __name__ == '__main__':
    result = parse_and_format_date('2023-10-5')
    print(result)
    result2 = parse_and_format_date('1999-1-1')
    print(result2)