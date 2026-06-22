from datetime import datetime

def format_date(year, month, day):
    date_obj = datetime(year, month, day)
    day_name = date_obj.strftime('%A')
    month_name = date_obj.strftime('%B')
    return f"{day_name}, {month_name} {day:02d}, {year}"

if __name__ == '__main__':
    result = format_date(2023, 10, 5)
    print(result)