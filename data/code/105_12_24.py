from datetime import datetime, timedelta

DAYS_IN_WEEK = 7

def get_next_weekday_date(reference_date_str: str, target_weekday_name: str) -> str:
    target_map = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6,
    }
    if target_weekday_name not in target_map:
        raise ValueError(f"Unsupported weekday name: {target_weekday_name}")
    
    target_weekday_num = target_map[target_weekday_name]
    current_date = datetime.strptime(reference_date_str, '%Y-%m-%d')
    current_weekday_num = current_date.weekday()
    
    days_to_add = (target_weekday_num - current_weekday_num + DAYS_IN_WEEK) % DAYS_IN_WEEK
    if days_to_add == 0:
        days_to_add = DAYS_IN_WEEK
        
    next_date = current_date + timedelta(days=days_to_add)
    return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    reference = '2023-10-01'
    target = 'friday'
    result = get_next_weekday_date(reference, target)
    print(result)