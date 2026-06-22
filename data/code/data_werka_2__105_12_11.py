from datetime import datetime, timedelta

TARGET_WEEKDAYS = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
}

def validate_weekday_name(name: str) -> int:
    normalized = name.lower()
    if normalized not in TARGET_WEEKDAYS:
        raise ValueError(f"Invalid weekday name: {name}")
    return TARGET_WEEKDAYS[normalized]

def compute_next_weekday(start_date_str: str, target_weekday_name: str) -> str:
    target_code = validate_weekday_name(target_weekday_name)
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    current_code = start_date.weekday()
    delta = (target_code - current_code) % 7
    if delta == 0:
        delta = 7
    result_date = start_date + timedelta(days=delta)
    return result_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    reference = '2023-10-01'
    target = 'friday'
    output = compute_next_weekday(reference, target)
    print(output)