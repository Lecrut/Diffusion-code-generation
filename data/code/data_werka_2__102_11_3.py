import datetime

def is_weekday(date_string: str) -> bool:
    parts = date_string.split('-')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date values")
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_date = "2023-10-07"
    result = is_weekday(sample_date)
    print(result)