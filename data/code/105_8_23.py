from datetime import date, timedelta

WEEKDAYS = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6
}

def find_next_weekday(target_name, start_date):
    if not isinstance(target_name, str):
        raise ValueError("target_name must be a string")
    if not isinstance(start_date, date):
        raise ValueError("start_date must be a date object")
    
    target_name_lower = target_name.lower()
    if target_name_lower not in WEEKDAYS:
        raise ValueError(f"Unknown weekday: {target_name}")
    
    target_index = WEEKDAYS[target_name_lower]
    current_index = start_date.weekday()
    
    days_until = (target_index - current_index) % 7
    if days_until == 0:
        days_until = 7
    
    next_date = start_date + timedelta(days=days_until)
    return next_date

if __name__ == '__main__':
    start_date = date(2023, 9, 15)
    target_day = "thursday"
    result = find_next_weekday(target_day, start_date)
    print(result)