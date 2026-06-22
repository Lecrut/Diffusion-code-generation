from datetime import datetime

def convert_date(date_str: str) -> str:
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    parts = date_str.split('/')
    if len(parts) != 3:
        raise ValueError("Date must have exactly three parts separated by slashes")
    month_str, day_str, year_str = parts
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        raise ValueError("Date components must be numeric")
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    try:
        dt = datetime(year, month, day)
    except ValueError:
        raise ValueError("Invalid date values")
    return dt.strftime("%Y-%m-%d")

if __name__ == '__main__':
    result = convert_date("01/15/2024")
    print(result)