from datetime import datetime

def format_date(date_obj):
    day_name = date_obj.strftime('%A')
    month_name = date_obj.strftime('%B')
    day = date_obj.day
    year = date_obj.year
    return f"{day_name}, {month_name} {day:02d}, {year}"

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 25)
    result = format_date(sample_date)
    print(result)