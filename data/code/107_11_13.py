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
    if day < 1:
        raise ValueError("Day out of range")
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif month in (4, 6, 9, 11):
        max_day = 30
    else:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        max_day = 29 if is_leap else 28
    if day > max_day:
        raise ValueError("Day out of range")
    return f"{year:04d}-{month:02d}-{day:02d}"

if __name__ == '__main__':
    result = convert_date("12/31/2023")
    print(result)