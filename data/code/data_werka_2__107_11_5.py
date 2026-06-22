import calendar

def convert_date(date_str: str) -> str:
    parts = date_str.split('/')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    month_str, day_str, year_str = parts
    try:
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)
    except ValueError:
        raise ValueError("Date components must be integers")
    if year < 1 or year > 9999:
        raise ValueError("Year out of range")
    if month < 1 or month > 12:
        raise ValueError("Month out of range")
    max_day = calendar.monthrange(year, month)[1]
    if day < 1 or day > max_day:
        raise ValueError("Day out of range for the given month")
    return f"{year:04d}-{month:02d}-{day:02d}"

if __name__ == '__main__':
    result = convert_date("02/29/2024")
    print(result)