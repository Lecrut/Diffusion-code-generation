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

def calculate_next_weekday_date(reference_str, target_name):
    target_val = WEEKDAY_NAMES.get(target_name.lower())
    if target_val is None:
        raise ValueError("Invalid weekday name provided")
    
    ref_date = datetime.strptime(reference_str, '%Y-%m-%d')
    current_val = ref_date.weekday()
    
    days_diff = (target_val - current_val) % 7
    if days_diff == 0:
        days_diff = 7
        
    next_date = ref_date + timedelta(days=days_diff)
    return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    ref = '2023-10-01'
    day = 'Friday'
    print(calculate_next_weekday_date(ref, day))