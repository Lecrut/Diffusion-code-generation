from datetime import date

def _validate_date_string(date_string: str) -> None:
    parts = date_string.split("-")
    if len(parts) != 3:
        raise ValueError("Invalid format")
    for part in parts:
        if len(part) != 4 or len(part) != 2:
            raise ValueError("Invalid format")
        int(part)

def get_day_of_week(date_string: str) -> int:
    _validate_date_string(date_string)
    parts = date_string.split("-")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    d = date(year, month, day)
    return d.weekday()

if __name__ == '__main__':
    print(get_day_of_week("2023-10-23"))
    print(get_day_of_week("2024-01-01"))
    print(get_day_of_week("2000-02-29"))