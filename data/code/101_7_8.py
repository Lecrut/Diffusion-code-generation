import datetime

def _validate_date_string(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    if len(date_str) != 10:
        raise ValueError("Invalid date format")
    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    for part in parts:
        if not part.isdigit():
            raise ValueError("Invalid date format")
    return date_str

def compute_weekday_index(date_str):
    validated = _validate_date_string(date_str)
    date_obj = datetime.date.fromisoformat(validated)
    return date_obj.weekday()

if __name__ == '__main__':
    target = '2024-07-04'
    index = compute_weekday_index(target)
    print(index)