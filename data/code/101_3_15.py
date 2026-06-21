from datetime import datetime

def get_weekday_name(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%A")
    except (ValueError, TypeError):
        raise ValueError(f"Invalid date string: {date_str}")

def _validate_date_string(date_str):
    if not isinstance(date_str, str) or len(date_str) != 10:
        raise ValueError("Date string must be a 10-character string")
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Date string must be in YYYY-MM-DD format")
    for part in parts:
        if not part.isdigit():
            raise ValueError("Date components must be digits")
    return True

if __name__ == '__main__':
    date_string = "2023-12-25"
    _validate_date_string(date_string)
    weekday = get_weekday_name(date_string)
    print(weekday)