from datetime import datetime

def validate_date_format(date_string):
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    parts = date_string.split('/')
    if len(parts) != 3:
        raise ValueError("Date must contain exactly two slashes")
    month_str, day_str, year_str = parts
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        raise ValueError("Date components must be numeric")
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}")
    if not (1 <= day <= 31):
        raise ValueError(f"Invalid day: {day}")
    if year < 1:
        raise ValueError(f"Invalid year: {year}")
    return True

def convert_date(date_string):
    validate_date_format(date_string)
    parsed_date = datetime.strptime(date_string, '%m/%d/%Y')
    return parsed_date.strftime('%d-%m-%Y')

if __name__ == '__main__':
    sample_date = '07/04/2024'
    result = convert_date(sample_date)
    print(result)