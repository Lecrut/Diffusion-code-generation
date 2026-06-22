from datetime import datetime, timedelta

def next_weekday(start_date_str, target_weekday_name):
    WEEKDAYS = {
        'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
        'friday': 4, 'saturday': 5, 'sunday': 6
    }
    if target_weekday_name not in WEEKDAYS:
        raise ValueError(f"Unknown weekday: {target_weekday_name}")
    
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    target_idx = WEEKDAYS[target_weekday_name]
    current_idx = start_date.weekday()
    
    days_offset = (target_idx - current_idx) % 7
    if days_offset == 0 and start_date.strftime('%A').lower() != target_weekday_name:
        days_offset = 7
        
    next_date = start_date + timedelta(days=days_offset)
    return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    result = next_weekday('2023-10-01', 'friday')
    print(result)