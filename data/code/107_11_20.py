def convert_date(date_str: str) -> str:
    parts = date_str.split('/')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    try:
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])
    except ValueError:
        raise ValueError("Date components must be integers")
    if year < 1:
        raise ValueError("Year out of range")
    if month < 1 or month > 12:
        raise ValueError("Month out of range")
    if day < 1:
        raise ValueError("Day out of range")
    max_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        max_days[2] = 29
    if day > max_days[month]:
        raise ValueError("Day out of range for given month")
    return f"{year:04d}-{month:02d}-{day:02d}"

if __name__ == '__main__':
    result = convert_date("02/29/2024")
    print(result)