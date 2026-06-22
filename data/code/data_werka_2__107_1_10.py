from datetime import datetime

def convert_date(date_string: str) -> str:
    if not date_string or len(date_string) != 10:
        raise ValueError("Invalid date format")
    parts = date_string.split('/')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    month, day, year = parts
    if not (month.isdigit() and day.isdigit() and year.isdigit()):
        raise ValueError("Invalid date format")
    month_int = int(month)
    if month_int < 1 or month_int > 12:
        raise ValueError("Invalid month")
    day_int = int(day)
    year_int = int(year)
    try:
        dt = datetime(year_int, month_int, day_int)
    except ValueError:
        raise ValueError("Invalid date")
    return dt.strftime('%d-%m-%Y')

if __name__ == '__main__':
    sample_date = '07/04/2022'
    result = convert_date(sample_date)
    print(result)