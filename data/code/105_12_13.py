from datetime import datetime, timedelta

def find_next_weekday(reference_date_str, target_weekday_name):
    valid_days = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }
    
    if target_weekday_name not in valid_days:
        raise ValueError(f"Invalid weekday name: {target_weekday_name}")
    
    try:
        ref_date = datetime.strptime(reference_date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Invalid date format: {reference_date_str}")
    
    target_index = valid_days[target_weekday_name]
    current_index = ref_date.weekday()
    
    days_to_add = (target_index - current_index) % 7
    
    if days_to_add == 0:
        days_to_add = 7
        
    next_date = ref_date + timedelta(days=days_to_add)
    
    return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    start = '2023-10-01'
    day = 'friday'
    output = find_next_weekday(start, day)
    print(output)