from datetime import datetime, timedelta

WEEKDAY_MAP = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
}

def get_next_weekday(start_date_str, target_weekday_name):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    
    if target_weekday_name not in WEEKDAY_MAP:
        raise ValueError(f"Unsupported weekday name: {target_weekday_name}")
    
    target_weekday = WEEKDAY_MAP[target_weekday_name]
    current_weekday = start_date.weekday()
    
    days_until_target = (target_weekday - current_weekday) % 7
    
    if days_until_target == 0:
        days_until_target = 7
    
    next_date = start_date + timedelta(days=days_until_target)
    return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    result = get_next_weekday('2023-10-01', 'friday')
    print(result)