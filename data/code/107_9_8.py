import calendar

def reformat_date(date_str):
    parts = date_str.split('-')
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    month_name = calendar.month_name[month]
    return f"{month_name} {day:02d}, {year}"

if __name__ == '__main__':
    sample_date = '2023-1-5'
    result = reformat_date(sample_date)
    print(result)