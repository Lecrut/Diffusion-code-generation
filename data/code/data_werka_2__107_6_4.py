from datetime import datetime

def format_date(day, month, year):
    date_obj = datetime(year, month, day)
    day_name = date_obj.strftime('%A')
    month_name = date_obj.strftime('%B')
    return f"{day_name}, {month_name} {day:02d}, {year}"

if __name__ == '__main__':
    result = format_date(15, 10, 2023)
    print(result)