from datetime import datetime, timedelta

WEEKDAY_NAMES = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
}

def validate_weekday_name(name):
    if not isinstance(name, str):
        raise ValueError("Weekday name must be a string")
    lower_name = name.lower().strip()
    if lower_name not in WEEKDAY_NAMES:
        raise ValueError(f"Invalid weekday name: {name}")
    return lower_name

def parse_date_string(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Date string must be a string")
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

def compute_days_until_target(current_weekday_idx, target_weekday_idx):
    diff = target_weekday_idx - current_weekday_idx
    if diff <= 0:
        return diff + 7
    return diff

def get_next_weekday(start_date_str, target_weekday_name):
    validated_name = validate_weekday_name(target_weekday_name)
    target_idx = WEEKDAY_NAMES[validated_name]
    start_date = parse_date_string(start_date_str)
    current_idx = start_date.weekday()
    days_to_add = compute_days_until_target(current_idx, target_idx)
    next_date = start_date + timedelta(days=days_to_add)
    return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    reference = '2023-10-01'
    target_day = 'friday'
    result = get_next_weekday(reference, target_day)
    print(result)